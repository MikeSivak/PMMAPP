from __future__ import print_function
import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

#Task (1)
# img = cv2.imread('./images/gel.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.01)
#
# #result is dilated for marking the corners, not important
# dst = cv2.dilate(dst,None)
# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.1*dst.max()]=[0,0,255]
# cv2.imshow('task 1',img)

#Task (2)
# img2 = cv2.imread('./images/gel.jpg')
# gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# corners = cv2.goodFeaturesToTrack(gray,40,0.01,10)
# corners = np.int0(corners)
# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(img2,(x,y),3,255,-1)
# cv2.imshow('task 2', img2)

# Task (3)
parser = argparse.ArgumentParser(description='Code for Affine Transformations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='./images/gel.jpg')
args = parser.parse_args()
src = cv2.imread(cv2.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)


srcTri = np.array( [[0, 0], [src.shape[1] - 1, 0], [0, src.shape[0] - 1]] ).astype(np.float32)
dstTri = np.array( [[0, src.shape[1]*0.33], [src.shape[1]*0.85, src.shape[0]*0.25], [src.shape[1]*0.15, src.shape[0]*0.7]] ).astype(np.float32)
warp_mat = cv2.getAffineTransform(srcTri, dstTri)
warp_mat2 = cv2.getAffineTransform(dstTri, dstTri);

warp_dst = cv2.warpAffine(src, warp_mat, (src.shape[1], src.shape[0]))
warp_dst2 = cv2.warpAffine(src, warp_mat2, (src.shape[1], src.shape[0]))
# Rotating the image after Warp
center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)
angle = 180
scale = 0.9
rot_mat = cv2.getRotationMatrix2D( center, angle, scale )
warp_rotate_dst = cv2.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))
warp_rotate_dst2 = cv2.warpAffine(warp_dst2, rot_mat, (warp_dst2.shape[1], warp_dst2.shape[0]))

cv2.imshow('Original image', src)
cv2.imshow('Warp', warp_dst)
cv2.imshow('Rotate', warp_rotate_dst2)
cv2.imshow('Warp + Rotate', warp_rotate_dst)


cv2.waitKey(0)