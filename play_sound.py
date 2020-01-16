import pygame
import wave
import time


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


play_sound(r"sounds/ohhayoo_01.wav", "wav")
