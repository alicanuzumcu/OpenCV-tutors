# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:35:18 2024

@author: ALI CAN
"""

import cv2
import numpy as np

img = cv2.imread('F.jpg',0)
img = cv2.resize(img, (640,480))

# Görüntüyü ikili (binary) formata dönüştür
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

contours, hierarch = cv2.findContours(binary_img, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(img.shape)
internal_contours = np.zeros(img.shape)

for i in range(len(contours)):
    
    #external contours
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contours, contours, i, (0, 255, 0), -1)
    
    #internal conturs
    else:
        cv2.drawContours(internal_contours, contours, i, 255, -1)
        
cv2.imshow('external', external_contours)
cv2.imshow('internal', internal_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()