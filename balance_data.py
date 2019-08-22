#!/usr/bin/env python3

import time

import cv2
import numpy as np
import os
import time
import pandas as pd
from collections import Counter

file_name = 'data/training_data_raw.npy'

train_data = np.load(file_name, allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))
