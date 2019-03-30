import pygame
pygame.mixer.init()
song = pygame.mixer.Sound("./ogg/b00.ogg")
song.set_volume(0.5)
clock = pygame.time.Clock()
while True:
    song.play()
    clock.tick(6000)

pygame.mixer.music.load('./wav/04.wav')   
pygame.mixer.music.set_volume(0.2)  # 设置音量
pygame.mixer.music.play()  # 播放音乐
pygame.time.Clock().tick(6000)
