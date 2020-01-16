import pygame
from pygame.locals import *
import wave
import time
import cv2


#音源ファイル再生
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


def main():
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return
### display.py からコピーした
    image_path="waifu.png"
    image_flag=1

    pygame.init()
    pygame.display.set_mode((10, 10), 0, 32)#1回modeをsetして画像をload

    image = pygame.image.load(image_path).convert()
    rect = image.get_rect()

    pygame.display.init()
    pygame.display.set_mode(rect[2:], 0, 32)
    screen = pygame.display.get_surface()
###
    #音声flag
    flag_hello = True

    camera = True
    window = True
    while camera or window:

        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #顔検出
        faces = face_cascade.detectMultiScale(gray, minSize=(200, 200))
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        #顔検出したら音源再生
        if len(faces):
            if flag_hello:
                play_sound("ohhayoo_01.wav", "wav")
                flag_hello = False

        if camera:    
            #frame表示
            cv2.imshow("", frame)

        #key入力
        key = cv2.waitKey(1) & 0xFF
        if key:
            #終了
            if key == ord('q'):
                #break
                camera = False
            #flagリセット
            elif key == ord('r'):
                flag_hello = True

        #ここからpygame
        if window:
            pygame.display.update()
            screen.fill((0, 0, 0))

            if len(faces):
                screen.blit(image, rect)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    window = False
                    break
    
    cap.release()
    cv2.destroyAllWindows()


main()