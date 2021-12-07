import sys
import numpy as np
import cv2
'''
# NLP
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

## ImagesToVideo
import cv2
import os
date = "2021"
image_folder = './'+keyword
video_name = 'video.avi'
'''

date = "2021"
keyword = "아라시 노래"

# importing libraries
import os
from PIL import Image

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("C:\\Users\\KOH\\PycharmProjects\\KoNLPy_tTV\\"+keyword+"\\"+date)
path = "C:\\Users\\KOH\\PycharmProjects\\KoNLPy_tTV\\"+keyword+"\\"+date

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))
# print(num_of_images)

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height
    # im.show()   # uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required because the video frame needs
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# embedded into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# print(mean_height)
# print(mean_width)

# Resizing of the images to give
# them same width and height
for file in os.listdir('.'):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
        # opening image using PIL Image
        im = Image.open(os.path.join(path, file))

        # im.size includes the height and width of image
        width, height = im.size
        print(width, height)

        # resizing
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
        imResize.save(file, 'JPEG', quality=95)  # setting quality
        # printing each resized image name
        print(im.filename.split('\\')[-1], " is resized")

    # Video Generating function


def generate_video():
    image_folder = '.'  # make sure to use your folder
    video_name = 'mygeneratedvideo.avi'
    os.chdir("C:\\Users\\KOH\\PycharmProjects\\KoNLPy_tTV\\"+keyword+"\\"+date)

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]

    # Array images should only consider
    # the image files ignoring others if any
    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    # Appending the images to the video one by one
    for i, image in enumerate(images):
            print(i, image)
            cap1 = images[i]
            cap2 = images[i+1]
            print(cap1, cap2)

            '''
            frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
            '''

            fps = cap1.get(cv2.CAP_PROP_FPS)
            effect_frames= int(fps*2)

            delay = int(1000 / fps)

            # 출력 동영상 객체 생성
            #video = cv2.VideoWriter(video_name, 0, 1, (width, height))
            out = cv2.VideoWriter('output.avi', 0, 1, (width, height))

            # 1번 동영상
            for i in range(cap1 - effect_frames):
                ret1, frame1 = cap1.read()

                if not ret1:
                    break

                out.write(frame1)
                cv2.imshow('frame', frame1)
                cv2.waitKey(delay)

            # 합성 과정
            for i in range(effect_frames):
                ret1, frame1 = cap1.read()
                ret2, frame2 = cap2.read()

                if not ret1 or not ret2:
                    print('frame read error!')
                    sys.exit()

                dx = int(width / effect_frames * i)

                # 디졸브 효과
                # 과중치를 이용. cv2.addWeighted 함수 이용하면 된다.
                alpha = i / effect_frames
                frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

                out.write(frame)
                cv2.imshow('frame', frame)
                cv2.waitKey(delay)

            # 2번 동영상
            for i in range(effect_frames, cap2):
                ret2, frame2 = cap2.read()

                if not ret2:
                    break

                out.write(frame2)


            #video.write(cv2.imread(os.path.join(image_folder, image)))

        # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated


# Calling the generate_video function
generate_video()