from konlpy.tag import Kkma
# 서울대학교 IDS(Intelligent Data System) 연구실에서 개발

# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()
text = "대학에서 DB, os, 데이터마이닝을 배웠는데욬ㅋ"

# 형태소 추출
morphs = kkma.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = kkma.pos(text)
print(pos)

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리
sentences = "어쩔티비! 무야호! 재밌다아앜ㅋㅋㅋ"
s = kkma.sentences(sentences)
print(s)
