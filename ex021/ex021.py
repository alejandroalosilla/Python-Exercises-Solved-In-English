# Ex021 - Write a Python program that opens and plays audio from an MP3 file.

import pygame


def playmusic():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('bob.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()


playmusic()
