[![author](https://img.shields.io/badge/author-Unperknown-lightgrey.svg)](https://github.com/Unperknown)
[![HitCount](http://hits.dwyl.io/Unperknown/AINOMOK.svg)](http://hits.dwyl.io/Unperknown/AINOMOK)
[![LICENSE](https://img.shields.io/dub/l/vibe-d.svg?style=flat-square)](https://github.com/Unperknown/AINOMOK/blob/master/LICENSE)
# AINOMOK

📜
**[View Entire Documentation](https://github.com/Unperknown/AINOMOK/blob/master/doc/Plan%20Document.pdf)**

2016년에 성행한 알파고와 이세돌과의 경기 모습에서 영감를 받아 오목을 두는 기계와 사람이 오목 게임을 할 수 있도록 한다. 기계는 인공지능이 내장된 데스크탑과 통신하여 실제 고수와 같이 게임하는 것 같이 구현하였다.

구현을 위한 영상 처리 기술과 인공 지능은 Python 라이브러리 OpenCV와 Tensorflow를 사용해 작성하였으며 기계 제어와 통신 프로세스는 Arduino의 GRBL쉴드를 사용하여 3D Printer와 흡사하게 작동 할 수 있도록 C언어로 작성하였다. 물리적 설계는 3D 모델링으로 Fusion 360을 사용하였다.

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
- [🔗Unperknown](https://github.com/Unperknown) : Image Processing, AI Development
- [🔗asphalt-alpha](https://github.com/asphalt-alpha) : Assembling Robot, 3D Modeling
- [🔗ohseyoung123](https://github.com/ohseyoung123) : Arduino Programming

### Others
- [🔗Las-Wonho](https://github.com/Las-Wonho) : Correction of document(README.md)
- [🔗cdb0915](https://github.com/cdb0915) : Arduino Programming Assistant

## 🔑Stack
  
- Python
  - Tensorflow(for C: Partically uses Ubuntu OS)
  - OpenCV

- Arduino

- 3D Printing & Modeling


## 🕤Daily Progress
### Day 1(12/27) - 계획서 수정 및 개발 과정 설계

##### 1. 계획서 버전 수정 및 브로슈어 추가

doc 디렉토리의 계획서를 10/24(Ver.1)에서 12/26(Ver.2)로 Commit하였다. 그리고 계획 수립 과정 중 판넬 구성을 하기로 결정함에 따라 브로슈어 원본을 추가하였다.

##### 2. 시스템 설계
**시스템 설계의 도식은 나중에 업데이트될 예정이다.**

구현은 오목 게임의 상태를 저장하고 제어하는 데스크탑과 물리적인 상태 저장과 출력을 담당하는 아두이노 간의 통신으로 이루어질 것이다. 데스크탑은 웹캠과 연결되어 웹캠에서 주어진 오목판의 이미지를 영상 처리하여 오목판을 저장하는 배열의 각 상태를 업데이트한다. 각 업데이트를 Round로 나누어 각 Round마다 데스크탑에 내장된 RL 모델이 컴퓨터가 둘 좌표를 판단하여 그 좌표를 아두이노에 전달한다.

아두이노는 전달한 좌표에 따라 모터를 제어하는 프로시저에 따라 바둑판의 상태에 알맞게 둔다. 아두이노의 LCD 패널에 게임이 진행 중인지, 끝났는지 표시한다. 그리고 버튼을 눌러 게임을 시작하는 신호나 중지하는 신호를 데스크탑으로 보낸다. 반대로 데스크탑은 오목 게임이 끝나는 Round에 게임이 끝났다는 신호를 아두이노로 보낸다.

### Day 2(12/28) - 개발 세팅 및 테스트 설계(단위 테스트)

##### 1. 부품 조달 확인

부품 조달이 지연되어 실전 테스팅은 시현 직전인 1월 5일부터 1월 7일까지 하기로 결정하였다. 부품이 오는 동안 프로세스의 구현과 RL 모델 훈련을 하는 것으로 결정하여 Day 3부터 본격적으로 개발하기로 하였다.

##### 2. 개발 환경 및 테스트

영상 처리: 테스트는 부품이 오지 않아 임시로 노트북의 웹캠으로 대신 테스트할 것이다. 이미지나 영상을 띄웠을 때 검은 돌과 하얀 돌이 어느 좌표에 있는지 CLI에 출력하는 것으로 단위 테스팅할 것이다.

RL 모델: 시간 내에 구현하지 못할 가능성을 방지하기 위해 시초에는 Python의 easyAI 라이브러리로 먼저 구현할 것이다. 그러고 나서 알맞게 리팩토링하여 Tensorflow 라이브러리로 재작성할 것이다.

3D 모델링: 로봇 하드웨어를 구성하는 부품의 구성을 모델링하여 저장소에 커밋하여 보관한다. 그러고 나서 출력하여 부품이 오는 즉시 조립을 시작할 것이다.

### Day 3 ~ Day 5(12/29, 1/2 ~ 1/3) - 개발 수행

##### 1. Unperknown - Image Processing

![영상 처리를 통한 바둑돌 감지](/doc/detection.png "바둑돌 감지 사진")

영상 처리를 통해 임시로 파란색을 감지하는 것을 성공하였다.(12/29) 그러고 나서 지속적인 색 감지 테스트를 통해 검은돌과 하얀돌의 위치를 화면으로 탐지할 수 있게 나는데 성공하였다.(1/3) 그러나 현재 하드웨어가 완성되지 않아 실제로 탐지되는지 테스트를 할 수 없는 상태이다. 색 탐지 값을 조정하는데 하드웨어에 설치된 스탠드의 빛의 밝기, 웹캠의 위치 등에 따라 상당히 달라질 수 있어 좌표의 색을 검출하여 오목판의 상태를 업데이트하는 프로세스는 AI 모델을 완성하고 게임 제어 프로그램을 구성한 후인 가장 마지막에 하기로 결정하였다.

현재 게임 제어 프로그램과 AI 모델은 src 디렉토리를 어떻게 구성할지에 대한 회의가 끝나고 나서 차근차근 커밋할 예정이다.

##### 2. ohseyoung123 - Arduino Programming

시리얼 통신을 C#로 작성하였다. 기본적인 틀을 숙지하고 나서 본격적으로 목적에 알맞게 구현할 것이다. 코드를 짜는데에 어려움을 겪어 검색과 친구들에게 물어봐가며 C++로 작성하려고 하였으나 지속적인 오류가 일어났다.(~1/2)방법을 찾던 중 선배의 도움을 받아 C#으로 작성할 수 있는 방법을 찾아 각 아두이노 핀으로 문자열을 출력하는 데에 성공하였다.(1/3)

##### 3. asphalt-alpha - 3D Modeling

부품을 모델링하였다. 저장소에 커밋하고 나머지 필요한 부품을 추가로 더 할 것이다.

### Day 6 ~ Day 8(1/4 ~ 1/6) - 개발 수행 및 테스트

##### 1. cdb0915 - Assistance of Arduino Programming

시리얼 통신을 구현을 검증하는 중에 ohseyoung123과의 협의를 거쳐 기술 한계 상 Python으로 재작성하자고 결정하였다.(1/4) 그래서 ohseyoung123이 작성한 소스 파일을 리뷰하고 현재 오목 제어 프로그램과 시리얼 통신 프로그램을 합치는 작업을 진행하고 있다.

##### 2. Unperknown - AI Development and Omok Program

하드웨어 안의 오목판의 상태를 담은 데이터를 가져와 현재 Round의 승리 여부를 확인하고 턴을 돌리는 제어 프로그램을 작성하였다.(12/28) 그 제어 프로그램에서 영상 처리를 통해 플레이어가 둔 돌의 좌표를 가져오는 메서드와 AI 모델을 실행하여 좌표를 가져오는 메서드는 현재 작업 중이다. 현재 모델이 훈련이 아직 되지 않았고 생겨난 버그를 수정하고 있다. (1/2 ~) 저번에 언급한 대로 내일(1/6)에 영상 처리를 통해 좌표를 불러오는 메서드를 실제 하드웨어에 연결해 테스트할 예정이다. 그러면서 그 메서드 소스 파일을 커밋할 것이다.

##### 3. asphalt-alpha - Assembling Robot

현재 설계도에 계획한 도면대로 대부분의 물리적 구현을 마치고 있다.(1/4 ~) 그러나 세세한 작업을 하면서 웹캠까지 다 설치하는데 시간이 걸려 최종적인 테스트는 내일(1/7) 하기로 하였다. 

### Day 8 ~ Day 9(1/7 ~ 1/8) - 프로젝트 일시 중단

하드웨어와 프로그램 간의 네트워크 구현이 원활하게 이루어지지 않았고 영상 처리 기술을 구현하는데 시간이 매우 촉박하였다. 그래서 프로토타입만 전시하기로 결정하였다.

### Day 10(5/14? ~ ) - 프로젝트 재개

각 팀원의 스케줄 문제로 2분기 방과후 프로그램에 프로젝트 반을 따로 구성하여 그 시간 동안 완성하기로 결정하였다. 정확한 재개 날짜는 아직 정해지지 않았다.
