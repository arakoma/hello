import pygame
from pygame.locals import *


#imageのサイズでwindow表示、image_flagは画像表示or黒画面
def display(image_path, image_flag):
    pygame.init()
    pygame.display.set_mode((10, 10), 0, 32)#1回modeをsetして画像をload

    image = pygame.image.load(image_path).convert()
    rect = image.get_rect()

    pygame.display.init()
    pygame.display.set_mode(rect[2:], 0, 32)
    screen = pygame.display.get_surface()

    window = True

    while window:
        pygame.display.update()
        screen.fill((0, 0, 0))

        if image_flag:
            screen.blit(image, rect)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                window = False
                break


display(image_path="waifu.png", image_flag=1)