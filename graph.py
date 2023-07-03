import matplotlib.pyplot as plt

accuracy = [0.8178, 0.9005, 0.9370, 0.9584, 0.9697, 0.9757, 0.9792, 0.9820, 0.9833, 0.9852]
val_accuracy = [0.8244, 0.8297, 0.8244, 0.8276, 0.8295, 0.8316, 0.8337, 0.8377, 0.8377, 0.8437]

loss = [0.3897, 0.2441, 0.1602, 0.1083, 0.0797, 0.0632, 0.0540, 0.0468, 0.0419, 0.0340]
val_loss = [0.9788, 0.9330, 0.8728, 0.8735, 0.8223, 0.7425, 0.6101, 0.5259, 0.4176, 0.3499]

plt.title('LSTM Accuracy')
plt.plot(accuracy, label='Train Accuracy')
plt.plot(val_accuracy, label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('LSTM_Accuracy.png')
plt.close()

plt.title('LSTM Loss')
plt.plot(loss, label='Train Loss')
plt.plot(val_loss, label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('LSTM_Loss.png')
plt.close()