# KoNLPy_tTV
text To Video / 텍스트를 입력하면 그에 맞는 영상을 보여줍니다.

![image](https://github.com/Junst/KoNLPy_tTV/blob/master/GitPic/%EA%B7%B8%EB%A6%BC1.jpg)

## 개요
현 인공지능에서 가장 크게 대두되고 있는 NLP(자연어 처리)는 아직도 무궁무진하게 많은 과제를 남겨두고 있다. 그 중 가장 범용성이 뛰어난 활용 사례로는 “TEXT 입력을 통한 다양한 출력 프로그램”이 될 것이다. 즉, 입력 받은 text를 분석하여 그것에 맞는 text 혹은 Picture, Video, IoT 등 다양한 출력 형태의 결과물을 만들어내는 것이다.

본 프로젝트는 이러한 활용 사례를 참조하여 text To Video (T-TV)를 만들고자 한다. 여러 기술들이 조합하여 들어가겠지만, 가장 핵심이 되는 기술은 NLP(자연어 처리)의 영어 BERT이다. BERT는 자연어의 양방향적 해석, 문맥을 고려한 분석이 가능한, 현 NLP 기술에서 널리 쓰이고 있는 모델이다. 따라서 이 기술을 통해 입력 받은 text를 고려하여 그에 걸맞는 Video를 연출하는 프로젝트를 진행하고자 한다. 또한 Video를 구현하기 전, 먼저 Picture를 통해 결과를 도출하는 소규모 달성과제 역시 진행하고자 한다.
입력에서의 필요한 장비는 Jetson Nano와 Keyboard이며, 출력에서의 필요한 장비는 Monitor와 CUDA 등의 그래픽 카드로 예상하고 있다. 또한 기술적 한계가 크지 않다면, 마이크를 통한 음성 인식 역시 구현하고자 한다.


## 프로세스
![image](https://github.com/Junst/KoNLPy_tTV/blob/master/GitPic/%EA%B7%B8%EB%A6%BC2.png)

1. KeyBoard(와 Microphone)을 통해 
Text Input을 받습니다.

2. 해당 Input을 Pytorch (NLP)로 분석
합니다. : KoNLPy 

3. 분석된 데이터의 주제를 구글에서
크롤링을 합니다. : Selenium

4. MoviePy라는 오픈소스를 통해 해당
사진을 영상으로 인코딩합니다.

5. Speaker와 Monitor로 결과물을 출
력합니다.


## 진행 과정
2021.11.24

KoNLPy에서 Noun_list 생성 및 배열을 통해 가장 빈도 수가 높은 단어를 체크합니다.
![image](https://github.com/Junst/KoNLPy_tTV/blob/master/GitPic/tTV_NLP1.png)

빈도 수가 높은 단어 2개를 단순히 합쳤습니다.
![image](https://github.com/Junst/KoNLPy_tTV/blob/master/GitPic/tTV_NLP2.png)



... 개발 진행 중 (2021. 10 ~ )
