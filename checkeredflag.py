#!/usr/bin/env python3

import time

def countdown(seconds):
    print('Starting in')
    while seconds > -1:
        time.sleep(1)
        if seconds == 0:
            print()
            print('GO!')
        else:
            print(seconds)

        seconds = seconds - 1
