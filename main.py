import pygame
from pygame.locals import *
import wave
import time
import cv2
import numpy as np

import my_func


def main():
    # 設定画面
    img_path = my_func.configuration()

    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    
    # カメラ調整の時間
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return
    f = "adjust camera ! if ok, push s key"
    while True:
        ret, frame = cap.read()
        cv2.namedWindow(f, cv2.WINDOW_NORMAL)
        cv2.imshow(f, frame)
        #key入力
        key = cv2.waitKey(1) & 0xFF
        if key:
            #終了
            if key == ord('s'):
                break
    cap.release()
    cv2.destroyAllWindows()

    #表示画像
    img_in = cv2.imread(img_path)
    img_out = my_func.mosaic(img_in, s=1)

    #音声flag
    flag_hello = True

    # 顔検出フラグ
    flag_inout = False
    
    # 時間測る
    start_in = time.time()
    start_out = time.time()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    f = "q:quit, r:reset,"
    while True:

        ret, frame = cap.read()

#        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #顔検出
        faces = face_cascade.detectMultiScale(gray, minSize=(200, 200))
#        for (x,y,w,h) in faces:
#            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        t_lim = 3
        now = time.time()
        t_in = now - start_in
        t_out = now - start_out

        #顔検出t_lim秒以上連続同じ場合
        if len(faces) and t_in >= t_lim:
            if flag_inout:
                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_in)
            else:
                # appear
                for s in range(1, 30):
                    img2 = my_func.mosaic(img_in, s)
                    cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                    cv2.imshow(f, img2)
                    cv2.waitKey(50)

                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_in)
                flag_inout = True
                start_in = now - t_lim
                
                # flag で音声出力
                if flag_hello:
                    my_func.play_sound(r"sounds/ohhayoo_01.wav", "wav")
                    flag_hello = False

            start_out = time.time()
        
        elif not len(faces) and t_out >= t_lim:
            if not flag_inout:
                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_out)
            else:
                # disappear
                for s in range(1, 30)[::-1]:
                    img2 = my_func.mosaic(img_in, s)
                    cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                    cv2.imshow(f, img2)
                    cv2.waitKey(50)
                
                flag_inout = False
                start_out = now - t_lim
            start_in = time.time()
        
        # t_lim秒以上連続でない場合
        else:
            if flag_inout:
                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_in)
            else:
                cv2.namedWindow(f, cv2.WINDOW_NORMAL)
                cv2.imshow(f, img_out)

        #frame表示
#        cv2.namedWindow("", cv2.WINDOW_NORMAL)
#        cv2.imshow("", frame)

        #key入力
        key = cv2.waitKey(1) & 0xFF
        if key:
            #終了
            if key == ord('q'):
                break
            #flagリセット
            elif key == ord('r'):
                flag_hello = True

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()