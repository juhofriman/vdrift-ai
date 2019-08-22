#!/usr/bin/env python3

from pynput import keyboard

left = 0
right = 0
up = 0
down = 0
def on_press(key):
    global left, right, up, down
    if(key == keyboard.Key.left):
        left = 1
    if(key == keyboard.Key.right):
        right = 1
    if(key == keyboard.Key.up):
        up = 1
    if(key == keyboard.Key.down):
        down = 1


def on_release(key):
    global left, right, up, down
    if(key == keyboard.Key.left):
        left = 0
    if(key == keyboard.Key.right):
        right = 0
    if(key == keyboard.Key.up):
        up = 0
    if(key == keyboard.Key.down):
        down = 0

def kb_state():
    return [left, right, up, down]

def start_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
