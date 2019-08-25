#!/usr/bin/env python3

import time

import cv2
import mss
import numpy as np
import keypress as kb
import os
import checkeredflag as cf
from alexnet import alexnet
from pynput.keyboard import Key, Controller

keyboard = Controller()

WIDTH=319
HEIGHT=20
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'data/vdrift-{}-{}-{}.model'.format(LR, 'alexnetv2', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

shutdown = True

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 120, 'left': 0, 'width': 800, 'height': 450}

    breaks = 0

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array

        y = 90
        x = 0
        w = 319
        h = 20

        img = cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_BGR2GRAY)
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(img, dim)
        # canny = cv2.Canny(resized, 170, 50)
        crop_img = resized[y:y+h, x:x+w]
        (thresh, blackAndWhiteImage) = cv2.threshold(crop_img, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow('robot vision', blackAndWhiteImage)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            shutdown = not shutdown

        if shutdown:
            continue

        prediction = model.predict([blackAndWhiteImage.reshape(WIDTH, HEIGHT, 1)])[0]
        # print(prediction)
        moves = list(np.around(prediction))
        if moves == [1, 0, 0, 0]:
            print("left")
            keyboard.press(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.up)
            keyboard.release(Key.down)
        elif moves == [0, 1, 0, 0]:
            print("right")
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            keyboard.release(Key.up)
            keyboard.release(Key.down)
        elif moves == [0, 0, 1, 0]:
            print("forward")
            keyboard.press(Key.up)
            keyboard.release(Key.right)
            keyboard.release(Key.left)
            keyboard.release(Key.down)
        elif moves == [0, 0, 0, 1]:

            breaks = breaks + 1
            if(breaks > 40):
                print("Should break but run")
                keyboard.press(Key.up)
                keyboard.release(Key.right)
                keyboard.release(Key.left)
                keyboard.release(Key.down)
            else:
                print("break!")
                keyboard.press(Key.down)
                keyboard.release(Key.up)
                keyboard.release(Key.left)
                keyboard.release(Key.right)

            if(breaks > 70):
                breaks = 0


# while(True):
#     screen = np.array(ImageGrab.grab(bbox=(20,220, 420, 450)))
#
#     last_time = time.time()
#     print('Frame took {} seconds'.format(time.time() - last_time))
#     # cv2.imshow('window', cv2.resize(cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY), (80, 60)))
#     screen = cv2.resize(cv2.cvtColor(screen, cv2.COLOR_RGBA2GRAY), (80, 60))
#
#     prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
#     moves = list(np.around(prediction))
#     print(moves, prediction)
#
#     if moves == [1.0, 0, 0]:
#         keyboard.press('a')
#         keyboard.release('s')
#     elif moves == [0, 1.0, 0]:
#         keyboard.press('s')
#         keyboard.release('a')
#     elif moves == [0, 0, 1.0]:
#         keyboard.release('a')
#         keyboard.release('s')
