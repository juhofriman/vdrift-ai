#!/usr/bin/env python3

import time

import cv2
import mss
import numpy as np
import keypress as kb
import os
import checkeredflag as cf

file_name = 'data/training_data_raw.npy'

if(os.path.isfile(file_name)):
    print('File exists')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exists')
    training_data = []

cf.countdown(5)
# Comment out if cv2.imshow is used for testing
kb.start_listener();

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 120, 'left': 0, 'width': 800, 'height': 450}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array

        img = cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_BGR2GRAY)
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(img, dim)
        # cv2.imshow('OpenCV/Numpy edges', resized)

        print('fps: {0}'.format(1 / (time.time()-last_time)))

        training_data.append([resized, kb.kb_state()])

        if len(training_data) % 100 == 0:
            print("Saving slice of training data. Length: " + str(len(training_data)))
            np.save(file_name, training_data)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
