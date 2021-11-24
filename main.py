'''# NLP
from KoNLPy.KoNLPy_Okt import NLP

text = input()
NLP(text)
keyword = NLP(text)

# 크롤링
from Crawling.Crawling import checking, crawling, filtering, playing_mp3

crawling(keyword)
filtering(keyword)
playing_mp3(keyword)
# 아라시가 좋아요. 아라시의 노래 중에 가장 좋아하는 노래는 아라시입니다. 아라시의 아라시, 제목과 노래가 똑같아욬ㅋㅋㅋ
'''
## moviepy clips
import cv2
import os
keyword = "아라시 노래/2021.11.24/"
image_folder = './'+keyword
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()