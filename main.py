import pygame
from pygame.locals import *
import wave
import time
import cv2
import numpy as np
import os
import sys

import my_func


# .specのdatasの展開先pathの取得、_MEIPASSは.exeの起動時にpyinstallerが一時的に作るフォルダ
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def main():
    face_cascade = cv2.CascadeClassifier(resource_path('haarcascade_frontalface_default.xml'))
#    face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

    while True:
        # 設定画面
        img_path = my_func.configuration()
        if not os.path.exists(img_path):
            return

        # カメラ位置調整
        my_func.adjust_camera(face_cascade)

        #表示画像
        img_in = cv2.imread(img_path)
        img_out = my_func.mosaic(img_in, s=1)

        #音声flag
        flag_hello = True

        # 顔検出フラグ
        flag_sitting = False
        
        # 着席開始時間, 離席開始時間
        start_in = time.time()
        start_out = time.time()

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return

        f = "q:quit, r:reset, c:configuration"


        while True:

            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #顔検出
            faces = face_cascade.detectMultiScale(gray, minSize=(200, 200))
    #        for (x,y,w,h) in faces:
    #            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            
            t_lim = 3
            now = time.time()
            t_in = now - start_in
            t_out = now - start_out

            #顔検出ありt_lim秒以上連続の時
            if len(faces) and t_in >= t_lim:
                if not flag_sitting:
                    # appear
                    for s in range(1, 30):
                        img2 = my_func.mosaic(img_in, s)
                        cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                        cv2.imshow(f, img2)
                        cv2.waitKey(50)
                    flag_sitting = True
                    start_in = now - t_lim
                
                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_in)

                # flag で音声出力
                if flag_hello:
                    my_func.play_sound(resource_path("ohhayoo_01.wav"), "wav")
#                    my_func.play_sound("./sounds/ohhayoo_01.wav", "wav")

                    flag_hello = False

                start_out = time.time()
            
            #顔検出なしt_lim秒以上連続の時
            elif not len(faces) and t_out >= t_lim:
                if flag_sitting:
                    # disappear
                    for s in range(1, 30)[::-1]:
                        img2 = my_func.mosaic(img_in, s)
                        cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                        cv2.imshow(f, img2)
                        cv2.waitKey(50)
                    flag_sitting = False
                    start_out = now - t_lim
                
                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_out)

                start_in = time.time()
            
            # t_lim秒以上連続で同じじゃない場合
            else:
                if flag_sitting:
                    cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                    cv2.imshow(f, img_in)
                else:
                    cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                    cv2.imshow(f, img_out)

            #key入力
            key = cv2.waitKey(1) & 0xFF
            if key:
                #終了
                if key == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    return
                #flagリセット
                elif key == ord('r'):
                    flag_hello = True
                #設定画面に戻る
                elif key == ord('c'):
                    break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()