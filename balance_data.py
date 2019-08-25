#!/usr/bin/env python3

import time

import cv2
import numpy as np
import os
import time
import pandas as pd
from collections import Counter
from random import shuffle

file_name = 'data/training_data_simple.npy'

train_data = np.load(file_name, allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

shuffle(train_data)

lefts = []
rights = []
forwards = []
brakes = []

for data in train_data:
    img = data[0]
    choice = data[1]

    if(choice[0] == 1): #[1, 0, 0, 0]):
        lefts.append([img, [1, 0, 0, 0]])

    if(choice[1] == 1): # [0, 1, 0, 0]):
        rights.append([img, [0, 1, 0, 0]])

    if(choice == [0, 0, 1, 0]):
        forwards.append([img, [0, 0, 1, 0]])

    if(choice[3] == 1): # [0, 0, 0, 1]):
        brakes.append([img, [0, 0, 0, 1]])

forwards = forwards[:len(lefts)][:len(rights)][:len(brakes)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
brakes = brakes[:len(forwards)]

final_data = forwards + lefts + rights + brakes

shuffle(final_data)

df = pd.DataFrame(final_data)
print(df.head())
print(Counter(df[1].apply(str)))

np.save('data/training_data-balanced.npy', final_data)
