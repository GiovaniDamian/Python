#Primeiro colar o áudio para o projeto(botão direito\Pasta)
import pygame
pygame.mixer.init()
pygame.base.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()