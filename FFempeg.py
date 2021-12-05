import os
os.system("ffmpeg -f image2 -r 28 -i /arashisong/2021.11.24/%03d.jpg -vcodec"
          " mpeg4 -y /path_convert_video.mp4")


'''
-f : 입력 파일의 포맷 의미, image2는 jpg 파일 의미
-r : 출력 동영상 fps 지정
-i : 입력 파일 위치 및 형식 %04d.jpg는 4자리 숫자로 구성된 jpg 파일을 의미한다. (ex. 0000.jpg, 0001.jpg, ..., 9999.jpg)
-vcodec : 출력 동영상의 압축 코덱을 의미, H.264가 가장 무난하다고 함

'''