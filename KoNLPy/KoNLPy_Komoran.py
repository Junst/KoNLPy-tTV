from konlpy.tag import Komoran
# Shineware에서 개발하였다.

'''
# 코모란 형태소 분석기 객체 생성
komoran = Komoran()
text = "간다라 미술은 무엇일까요?"

# 형태소 추출
morphs = komoran.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print(pos)

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)
'''

komoran = Komoran(userdic='./user_dic.tsv')
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komoran.pos(text)
print(pos)