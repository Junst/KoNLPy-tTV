from konlpy.tag import Okt
# 오픈 소스 한국어 분석기
# 속도는 느리지만, 정규화에 매우 좋음

# Okt 형태소 분석기 객체 생성
okt = Okt()
text = "김치 냉장고 앞에서 최면!"

# 형태소 추출
morphs = okt.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print(pos)

# 명사만 추출
nouns = okt.nouns(text)
print(nouns)

# 정규화, 어구 추출
text = "하나 둘 셋 장고!"
print(okt.normalize(text))
print(okt.phrases(text))