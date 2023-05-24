import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.keras import models, layers, optimizers, losses, metrics
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import csv
from tensorflow.keras.layers import Dense, Embedding, Flatten, LSTM, Dropout
from tensorflow.keras import Input, Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt

x, y = [], []
file1 = "./comment-labeling.csv"
file2 = "./naver-ratings.csv"

f = open(file1, 'r', encoding='utf-8')
read = csv.reader(f)
for line in read:
    emotion = float(line[-1])
    x.append(line[0])
    y.append(emotion)

f.close()

x2, y2 = [], []
f = open(file2, 'r', encoding='utf-8')
read = csv.reader(f)
for line in read:
    emotion = float(line[-1])
    y2.append(emotion)
    x2.append(line[0])

f.close()

test_percent = 0.2

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_percent)
a, b, c, d = train_test_split(x2, y2, test_size=test_percent)

x_train += a
x_test += b
y_train += c
y_test += d


def build_model(train_data):
    train_data = tf.data.Dataset.from_tensor_slices(train_data)
    model = Sequential()
    model.add(Input(shape=(1,), dtype="string"))
    max_tokens = 15000
    max_len = 50
    vectorize_layer = TextVectorization(
        max_tokens=max_tokens,
        output_mode="int",
        output_sequence_length=max_len
    )

    vectorize_layer.adapt(train_data.batch(64))
    model.add(vectorize_layer)
    model.add(layers.Embedding(max_tokens + 1, output_dim=200))
    model.add(LSTM(64, return_sequences=True))
    model.add(layers.Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(8, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    return model

tf.config.experimental_enable_xla=True

early_stop = EarlyStopping(monitor='val_loss', patience=3)
checkpoint = ModelCheckpoint(filepath='model_{epoch:02d}', save_format='tf', monitor='val_accuracy', save_best_only=False)

rnn_model = build_model(x_train)
rnn_model.compile(
    optimizer="adam",
    loss='binary_crossentropy',
    metrics=['accuracy']
)

rnn_model.summary()

history = rnn_model.fit(
    x_train,
    y_train,
    epochs=50,
    batch_size=128,
    validation_data=(x_test, y_test),
    callbacks=[early_stop, checkpoint]
)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.savefig('LSTM_accuracy_plot.png')
plt.close()

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.savefig('LSTM_loss_plot.png')
plt.close()
