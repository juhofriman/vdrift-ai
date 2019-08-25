#!/usr/bin/env python3

import time

import cv2
import numpy as np
import os
import time


file_name = 'data/training_data_raw.npy'

training_data_raw = np.load(file_name, allow_pickle=True)
training_data = []
for [image, kb] in training_data_raw:

    y = 90
    x = 0
    w = 319
    h = 20

    # canny = cv2.Canny(image, 170, 50)
    crop_img = image[y:y+h, x:x+w]
    (thresh, blackAndWhiteImage) = cv2.threshold(crop_img, 127, 255, cv2.THRESH_BINARY)
    training_data.append([blackAndWhiteImage, kb])

np.save('data/training_data_simple.npy', training_data)
