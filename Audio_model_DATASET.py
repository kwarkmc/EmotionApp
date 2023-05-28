import os
import warnings

import numpy as np
from tensorflow import keras
import sklearn
from sklearn import preprocessing
from unicodedata import normalize
import tensorflow as tf
from keras import layers
from keras.utils import to_categorical
from tensorflow.python.keras.callbacks import TensorBoard
from keras.callbacks import EarlyStopping, ModelCheckpoint
import librosa
import matplotlib.pyplot as plt

os.environ["CUDA_VISIBLE_DEVICES"]="0"

warnings.filterwarnings(action='ignore')

def pad1d(a, i):
    return a[0:i] if a.shape[0] > i else np.hstack((a, np.zeros(i - a.shape[0])))

def pad2d(a, i):
    return a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i - a.shape[1]))))

class DataGenerator(keras.utils.Sequence):
	
	def __init__(self, data_path, batch_size, is_train):
		self.data_path = data_path
		self.batch_size = batch_size
		self.files = os.listdir(data_path)
		self.num_files = len(self.files)
		self.indexes = np.arange(self.num_files)
		self.is_train = is_train
	
	def __len__(self):
		return int(np.ceil(self.num_files / float(self.batch_size)))
	
	def __getitem__(self, index):
		batch_files = self.files[index*self.batch_size:(index+1)*self.batch_size]
		batch_data = []
		batch_labels = []
		for file in batch_files:
			if '.wav' not in file in file:
				continue
			data, sr = librosa.load(os.path.join(self.data_path, file), sr=16000)
			data = librosa.feature.mfcc(y=data, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
			data = preprocessing.scale(data, axis=1)
			data = pad2d(data, 700)

			if '긍' in file:
				label = 1
			elif ('부' in file):
				label = 0

			data = np.expand_dims(data, -1)
			label = np.expand_dims(label, -1)
			batch_data.append(data)
			batch_labels.append(label)
		batch_label = to_categorical(batch_labels, num_classes=2)
		return np.array(batch_data), np.array(batch_labels)

train_data_path = "1. VoiceToEmotion/Data/train_real"
test_data_path = "1. VoiceToEmotion/Data/test_real"
batch_size = 10

train_generator = DataGenerator(train_data_path, batch_size, is_train=True)
test_generator = DataGenerator(test_data_path, batch_size, is_train=False)

model = tf.keras.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 700, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l1(0.01)))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(2, activation='softmax'))

model.summary()

#tensorboard = TensorBoard(log_dir="logs/{}".format(time()))
early_stop = EarlyStopping(monitor='val_loss', patience=10)
checkpoint = ModelCheckpoint(filepath='model_{epoch:02d}.h5', monitor='val_accuracy', save_best_only=False)

opt = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])


# 모델 학습 예시
history = model.fit(train_generator, epochs=50, validation_data=test_generator, callbacks=[early_stop, checkpoint])

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.savefig('CNN_accuracy_plot.png')
plt.close()

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.savefig('CNN_loss_plot.png')
plt.close()

