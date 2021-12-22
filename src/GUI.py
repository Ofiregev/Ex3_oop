import json
import pygame

pygame.init()
pygame.fint.init()

Font = pygame.font.SysFont('ariel','15')

WIDTH, HIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HIGHT),depth=32)

while True:
    for event in pygame.event.get():

