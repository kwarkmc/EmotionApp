import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np


# 데이터셋 클래스 정의
class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).float()
        self.y = torch.from_numpy(y).float()

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.y[index]


# 모델 클래스 정의
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(32 * 49 * 231, 64)
        self.relu2 = nn.ReLU()
        self.fc2 = nn.Linear(64, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu2(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x


# 하이퍼파라미터 설정
num_epochs = 10
batch_size = 16
learning_rate = 0.001

# 데이터셋 및 데이터로더 생성
train_dataset = MyDataset(train_X_ex, train_y)
test_dataset = MyDataset(test_X_ex, test_y)
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

# 모델 및 손실함수, 최적화 알고리즘 정의
model = MyModel()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 학습
for epoch in range(num_epochs):
    for X, y in train_dataloader:
        # 모델에 입력값을 전달하여 예측값 계산
        y_pred = model(X)

        # 손실함수를 이용하여 손실 계산
        loss = criterion(y_pred, y)

        # 역전파 수행 및 가중치 업데이트
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # 검증 데이터셋을 이용하여 정확도 계산
    with torch.no_grad():
        correct = 0
        total = 0
        for X, y in test_dataloader:
            y_pred = model(X)
            predicted = torch.round(y_pred)
            total += y.size(0)
            correct += (predicted == y).sum().item()
        accuracy = 100 * correct / total

    # 로그 출력
    print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}, Accuracy: {accuracy:.2f}%")

# 모델 저장
torch
