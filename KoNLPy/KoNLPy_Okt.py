from konlpy.tag import Okt
# 오픈 소스 한국어 분석기
# 속도는 느리지만, 정규화에 매우 좋음

from collections import Counter

def NLP(text) :
    # Okt 형태소 분석기 객체 생성
    okt = Okt()

    #text = "냉장고 앞에서 최면!"
    '''
    # 형태소 추출
    morphs = okt.morphs(text)
    print(morphs)

    # 형태소와 품사 태그 추출
    pos = okt.pos(text)
    print(pos)
    '''
    # 명사만 추출
    nouns = okt.nouns(text)
    for i,v in enumerate(nouns):
        if len(v)<2:
            nouns.pop(i)
    count = Counter(nouns)

    print(nouns)

    # 명사 빈도 카운트
    noun_list = count.most_common(100)
    for v in noun_list :
        print(v)

    print("가장 높은 빈도 수의 단어 : ")
    print(noun_list[0])
    print("두 번째로 높은 빈도 수의 단어 : ")
    print(noun_list[1])
    print("두 단어를 합치기 : ")
    nouns_list= noun_list[0]+noun_list[1]
    print(nouns_list)

    '''
    # 정규화, 어구 추출
    text = "하나 둘 셋 장고!"
    print(okt.normalize(text))
    print(okt.phrases(text))
    '''

    return nouns_list, noun_list[0], noun_list[1]

text=input()
NLP(text)

