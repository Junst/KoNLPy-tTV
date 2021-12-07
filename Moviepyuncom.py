import os
import glob
from natsort import natsorted
from moviepy.editor import *

base_dir = os.path.realpath("./arashisong/2021.11.24")
print(base_dir)

gif_name = 'pic'
fps = 32

file_list = glob.glob(base_dir+'/'+'*.jpg')  # Get all the pngs in the current directory
file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images
print(file_list)

clips = [ImageClip(m).set_duration(2)
         for m in file_list_sorted]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=fps)