[![author](https://img.shields.io/badge/author-Unperknown-lightgrey.svg)](https://github.com/Unperknown)
[![HitCount](http://hits.dwyl.io/Unperknown/AINOMOK.svg)](http://hits.dwyl.io/Unperknown/AINOMOK)
[![LICENSE](https://img.shields.io/dub/l/vibe-d.svg?style=flat-square)](https://github.com/Unperknown/AINOMOK/blob/master/LICENSE)
# AINOMOK

📜
**[View Entire Documentation](https://github.com/Unperknown/AINOMOK/blob/master/doc/Plan%20Document.pdf)**

2016년에 성행한 알파고와 이세돌과의 경기 모습에서 영감를 받아 오목을 두는 기계와 사람이 오목 게임을 할 수 있도록 한다. 기계는 인공지능이 내장된 데스크탑과 통신하여 실제 고수와 같이 게임하는 것 같이 구현하였다.

구현을 위한 영상 처리 기술과 인공 지능은 Python 라이브러리 OpenCV와 Tensorflow를 사용해 작성하였으며 기계 제어와 통신 프로세스는 C++로 작성하였다. 물리적 설계는 3D 모델링 툴 을 사용하였다. 

## 📊Purpose

우리 학교 특성 상 소프트웨어 개발에 집중되어 있어 실제 기계에서 소프트웨어가 어떻게 활용되는지 알 수 없었는데 이번에 프로젝트를 진행하면서 알고 싶어서 로봇에 인공지능을 넣을 수 있도록 하였다.

그리고 조립한 기계 산출물이 전시회 이후에 사용되지 않고 버려지는 문제점에서 벗어나기 위해 보다 더 실용도가 높은 산출물을 개발하고 싶어서 최대한 흥미로운 아이디어를 접목하고 싶었다.

## ☑️Features
- 로봇은 오목판의 영상 처리를 통해 현재 상태를 분석하여
둘 수 있는 수 중 최적의 수를 전달한다.
- 구성품의 LCD 패널에서 출력되는 정보를 통해 현재 게임 스테이지의 상태를
알 수 있다.

## 🔘Entire Design
### Estimated Outputs
![예상 완성본](/Modeling/model.png "모델링 사진")

### System Design

## 👪Contributors

### Project Group
- [🔗Unperknown](https://github.com/Unperknown)
- [🔗asphalt-alpha](https://github.com/asphalt-alpha)
- [🔗ohseyoung123](https://github.com/ohseyoung123)

### Others
- [🔗Las-Wonho](https://github.com/Las-Wonho)

## 🔑Stack

- C++
  
- Python
  - Tensorflow(for C: Partically uses Ubuntu OS)
  - OpenCV

- Arduino

- 3D Printing & Modeling


## 🕤Daily Progress
### Day 1(12/27) - 계획서 수정 및 개발 과정 설계
### Day 2(12/28) - 개발 세팅 및 테스트 설계(단위 테스트)
### Day 3(12/29) - 개발 수행
