"""
自作関数

- configuration()
- play_sound(filename, type)
- mosaic(img, s=1, d=0)

"""

from tkinter import *
from tkinter import ttk
import os
import pygame
import wave
import time
import cv2
import numpy as np


# file存在確認(これはconfiguration()内で呼び出す関数)
def is_exist(path, frame, r, name):
    path = str(path.get())
    rpath = str(repr(path)[1:-1])#raw文字列化
    if os.path.exists(rpath):
        ok = ttk.Label(frame, width=50, text="{} ok !".format(name))
        ok.grid(row=r)
    else:
        no = ttk.Label(frame, width=50, \
                        text="no {}... please check the path".format(name))
        no.grid(row=r)


# 設定画面
def configuration():
    root = Tk()
    root.title("hello !")

    # メインフレーム(この中に諸々入れる)
    mainframe = ttk.Frame(root, padding=10)
    mainframe.grid()

    # 画像path入力
    label = ttk.Label(mainframe, text="image path :")
    label.grid(row=0)

    img_path = StringVar()
    entry_img_path = ttk.Entry(mainframe, width=50, textvariable=img_path)
    entry_img_path.grid(row=1)

    button_img_path = ttk.Button(mainframe, text="enter", \
                                command=lambda:is_exist(img_path, mainframe, 3, "image"))
    button_img_path.grid(row=2)

    # 終了
    button_fin = ttk.Button(mainframe, text="all ok", \
                                command=lambda:root.destroy())
    button_fin.grid(row=5)


    root.mainloop()

    img_path = str(img_path.get())
    r_img_path = str(repr(img_path)[1:-1])#raw文字列化

    return r_img_path


def play_sound(filename, type):

    if type == "wav":
        with wave.open(filename, "rb") as wav:
            frate = wav.getframerate()
            fnum = wav.getnframes()
            sound_time = fnum / frate
    
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(sound_time)
    pygame.mixer.music.stop()


# s*s個に分割する
# sは画像のサイズ以下にしてね
# 画像サイズをsで割り切れない場合、端はモザイクっぽくする
# 処理内容はほぼ mean pooling 
def mosaic(img, s=1, d=0):
    if len(img.shape) == 3:
        out = img.copy().astype(np.float32)
    if len(img.shape) == 2:
        out = img.copy().astype(np.float32)
        out = np.expand_dims(out, -1)

    H, W, C = out.shape
    
    dy = H // s
    dx = W // s
    for i in range(s):
        for j in range(s):
            for c in range(C):
                out[dy*i:dy*(i+1), dx*j:dx*(j+1), c] \
                    = np.mean(out[dy*i:dy*(i+1), dx*j:dx*(j+1), c])
    
    # 端を処理
    for i in range(H):
        for j in range(dx*s, W):
            out[i, j] = out[i, j-1]
    for i in range(dy*s, H):
        for j in range(W):
            out[i, j] = out[i-1, j]
    
    out += d
    
    #下限上限
    out = np.clip(out, 0, 255)

    out = out.astype(np.uint8)

    return out