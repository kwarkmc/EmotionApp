# 디지털 발자취를 이용한 감정 케어 플랫폼

<div align="center">
<img width="329" alt="image" src="https://github.com/kwarkmc/HelpDefault/blob/main/templates/defal.jpg?raw=true">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fkwarkmc%2FEmotionApp&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

# EmotionApp
> **한양대학교 ERICA 전자공학부 2023년도 캡스톤 디자인 2 결과물** <br/> **팀 핫둘셋얏**

## 팀 멤버 소개

|      18학번 곽민창       |          18학번 김지호         |          18학번 이승렬         |
|:---:|:---:|:---:|
   <img width="320px" src="https://avatars.githubusercontent.com/u/41298500?v=4" />|<img width="320px" src="https://avatars.githubusercontent.com/u/124140035?v=4" />|<img width="320px" src="https://avatars.githubusercontent.com/u/124139834?v=4" />|
|   [@kwarkmc](https://github.com/kwarkmc)   |    [@kjh-0523](https://github.com/kjh-0523)  |    [@leeseungry](https://github.com/leeseungry)  |
| 한양대학교 ERICA 전자공학부      4학년 | 한양대학교 ERICA 전자공학부     4학년 | 한양대학교 ERICA 전자공학부     4학년 |

## 한양대학교 ERICA 전자공학부 2023년도 캡스톤 디자인 2

**한양대학교 ERICA 공학대학 전자공학부** 에서 22년도 2학기 ~ 23년도 1학기에 걸쳐 개발한 졸업 작품 및 결과물. 통신 트랙 Hu Jin 교수님 지도하에 프로젝트가 진행되었으며, 통신 트랙 내에서 진행한 캡스톤 경진 대회를 통해 출품 및 결과물 PT를 진행하였다.

## 프로젝트 소개

학회방에 배치되어 있는 각종 공구 및 소자를 신규 학회원들로 하여금 선배들의 도움 없이 쉽고 간편하게 사용할 수 있도록 사용을 돕고, 금방 더러워지는 학회방을 깨끗하게 유지하고 공구 및 소자를 분실하지 않도록 정리를 돕는 서비스를 개발했다.

직접 학회방에 있는 각종 공구 및 소자의 사진을 여러 각도 및 형태에 따라 다양하게 촬영하여 11개의 Label에 대해 **Custom DataSet**을 구성하여 학습에 사용하였다.

빠른 학습 및 높은 Accuracy를 위하여 VGG-16 Model 의 Pre-Trained 데이터를 사용하여 **전이학습 (Transfered - Learning)** 을 활용하여 데이터를 학습하였다.

## 시작 가이드 🚩
### Requirements
For building and running the application you need:

- [Anaconda3](https://www.anaconda.com/download/)
- [Pytorch 2.0](https://pytorch.org/)
- [Jupyter Notebook](https://jupyter.org/)
- [Pycharm](https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows)

### Installation
``` bash
$ git clone git@github.com:kwarkmc/EmotionApp.git
$ cd EmotionApp
```
#### 서버 실행
``` bash
$ python ./multiserver.py
$ python ./pipeLine.py
```
#### 오디오 데이터 전처리
``` bash
$ python ./Audio_preprocess.py
```
#### 모델 학습
``` bash
$ python ./Audio_model.py # 음성 모델 학습
$ python ./Text_model.py # 텍스트 모델 학습
```

---

## Stacks 📚

### Environment
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
   

### Framework
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

### Development
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

### Communication
![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)          

---
## RESULT 📺
| Loss Graph  |  Accuracy Graph   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://github.com/kwarkmc/HelpDefault/blob/main/Document/pic/Loss.png?raw=true"/> |  <img width="329" src="https://github.com/kwarkmc/HelpDefault/blob/main/Document/pic/acc.png?raw=true"/>|  
| Flask API를 이용하여 웹서버 구현   |  RESULT   |  
| <img width="329" src="https://github.com/kwarkmc/HelpDefault/blob/main/Document/pic/flask.png?raw=true"/>   |  <img width="329" src="https://github.com/kwarkmc/HelpDefault/blob/main/Document/pic/result.png?raw=true"/>     |

> VGG-16의 Pretrained 데이터를 사용하여 전이학습을 진행했기 때문에 Accuracy는 2 epoch 만에, val_accuracy 또한 8 epoch 만에 좋은 값을 만들어내고 있다.
---
## 주요 기능 📦

### ❗ Custom DataSet을 폴더에서 Open 하여 Data와 Label로 준비
- 각 폴더 (t1 ~ t11) 에 Labeling 되어있고, OS API를 Import 하여 11개의 라벨에 맞춰 병합
- 학습에 사용하기 위해 `data.Dataset` 를 이용하여 `DefaultDataset` Class 를 만들어 Batch Size로 데이터를 쪼개서 불러와 사용함으로서 학습을 진행하는 PC의 메모리 제한에 좀 더 유연하게 코드를 실행시킬 수 있다.
- train / Test / Validation 데이터를 `DefaultDataset` Class를 이용하여 나눠서 구현
- 학습에 대한 검증은 Validation 데이터로, 실전 정확도는 Test 데이터를 사용하여 Overfitting을 방지할 수 있다.

### ❗ 데이터 증강 테크닉 사용
- `ImageTransform()` 클래스의 `self.data_transform` 을 이용하여 **Resize / Scale / Flip / Normalize** 등의 CV적 Augmentation을 진행하여 학습에 사용하였다.

### ❗전이학습 (Transfered - Learning)
- **VGG - 16** 모델의 Pre trained Model을 사용하여 마지막 레이어만 우리가 원하는 형태의 Input Data와 Label로 바꿔서 사용함으로서 이미 이미지 분류에 특화된 VGG - 16이 방대한 양의 이미지를 Classification 하는데 만들어낸 Weight 들을 사용하여 빠른 속도로 좋은 Accuracy를 만들어낼 수 있다.

### ❗ 모델을 H5 파일로 저장하여 Weight만 예측에 사용
- 각 epoch 마다 weight 파일을 H5 파일로 저장하고, Accuracy와 Loss를 csv 형태의 log로 남겨, 정해진 50 epoch의 학습이 종료되면 log file을 확인하고 **원하는 Accuracy와 Loss**에 해당하는 epoch의 weight 값을 예측에 사용할 수 있다.

### ❗Flask를 이용한 웹서버 구현
- Python 기반의 `Flask API`를 사용하여 쉽게 사용자가 사용할 수 있는 웹 서버를 구현하였다.
- 사용자는 웹 사이트에 들어가 사진을 찍거나, 업로드할 수 있다.
- 서버의 도착한 사용자의 이미지는 학습된 모델을 사용하여 업로드 된 사진의 라벨링 정보를 취득한다.
- 라벨링 정보를 조건문으로 처리하여 Label 1 ~ 11까지의 html 문서로 연결한다.
- 각 HTML 문서에는 해당하는 Label의 공구 및 소자의 사용 방법과 정리 위치가 기술되어 있다.