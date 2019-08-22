#!/usr/bin/env python3

import time

import cv2
import numpy as np
import os
import time


file_name = 'data/training_data_raw.npy'

training_data = np.load(file_name, allow_pickle=True)

for [image, kb] in training_data:

    y = 90
    x = 0
    w = 319
    h = 20

    canny = cv2.Canny(image, 170, 50)
    crop_img = canny[y:y+h, x:x+w]
    hough = np.zeros_like(canny)
    minLineLength = 20
    maxLineGap = 2
    lines = cv2.HoughLinesP(canny,1,np.pi/180,100,minLineLength,maxLineGap)
    if lines is None:
        lines = [[]]
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(hough,(x1,y1),(x2,y2),255,1)
    cv2.imshow('image', canny)
    cv2.imshow('crop', crop_img)
    cv2.imshow('hough', hough)
    # print(screen)
    print(kb)
    time.sleep(0.01)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
