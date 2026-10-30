import pygame, sys, time
from pygame.math import Vector2

pygame.init()


ScreenSize = 600

Screen = pygame.display.set_mode((800, ScreenSize))
pygame.display.set_caption('Orbit test')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Screen.fill((0,0,0))
    pygame.draw.circle(Screen,(100,100,100),(0,0),100)
    pygame.display.update()
    clock.tick(60)