import os
import pygame
import time
import random
mixer = pygame.mixer
player = mixer.music

class Player():
    __soundList = []
    __clock = pygame.time.Clock()

    def __init__(self):
        """
        初始化音频信息
        """
        pygame.init() 
        mixer.init()
        path='./ogg'
        oggFiles = os.listdir(path) 
        for item in oggFiles:
            if not os.path.isdir(item):
                sound = mixer.Sound(path +'/' + item)
                sound.set_volume(0.5)
                self.__soundList.append(sound)
                
    
    def play(self, idx):
        if idx < 0 or idx >= len(self.__soundList):
            raise Exception("Invalid Note", idx)
        sound = self.__soundList[idx]
        sound.play()
        self.__clock.tick(1) 
        



