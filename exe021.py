'''
Inserir um som no Python.
Só que não funcionou.
'''

import pygame
pygame.init()
pygame.mixer.music.load('exe0211.mp3')
pygame.mixer.music.play()
pygame.event.wait()

