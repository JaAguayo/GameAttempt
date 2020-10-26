# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:25:44 2020

@author: 19158
"""

import pygame 

Window_width = 1500
Window_height = 600
animation_increment = 10
clock_tik_rate = 20
clock = pygame.time.Clock()

pygame.init()
size = (Window_width, Window_height)
screen = pygame.display.set_mode(size)

dead = False



char = pygame.image.load('standing.png')

width = 192
height = 192
vel = 5
walkCount = 0

walkRight = [pygame.image.load('standing2.png'), pygame.image.load('standing3.png')]

def redrawGaneWindow():
    global walkCount
    if walkCount + 1 >= 2:
        walkCount = 0
        
    if right:
        screen.blit(walkRight[walkCount//3], (0, 400))
        walkCount += 1





while(dead == False):
    clock.tik(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            
    clock = pygame.time.Clock()
    #background_image = pygame.image.load("city.png"); #load an image
    pygame.display.set_caption("Game")
    
    pygame.display.flip()
    
    screen.blit(char, (0, 400))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        






pygame.quit()
