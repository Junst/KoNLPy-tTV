#ORB

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("000.png")
img2 = cv2.imread("001.png")

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

plt.imshow(img1_gray)
plt.imshow(img2_gray)

# Create our ORB detector and detect keypoints and descriptors
orb = cv2.ORB_create()

# Find keypoints and descriptors with ORB
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

# Create a BFMatcher object.
# It will find all of the matching keypoints on two images
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING,crossCheck=True)

matches = bf.match(descriptors1, descriptors2)

single_match = matches[0]
single_match.distance

matches = sorted(matches,key=lambda x:x.distance)

ORB_matches =cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:30], None, flags=2)
plt.imshow(ORB_matches)


