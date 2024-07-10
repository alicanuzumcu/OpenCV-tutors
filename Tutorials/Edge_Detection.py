# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:12:14 2024

@author: ALI CAN
"""
#import library
import cv2

#Load image
img = cv2.imread('F.jpg')
img = cv2.resize(img, (640,480))

#Find edges
edges = cv2.Canny(img,220,220)

#Apply Blur to diminish noise
blurred = cv2.blur(edges, ksize=(2,2))

#Visualize it!
cv2.imshow('Photo',blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
