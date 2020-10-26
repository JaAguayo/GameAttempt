# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:25:44 2020

@author: 19158
"""

import pygame 

Window_width = 700
Window_height = 500

pygame.init()
size = (Window_width, Window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

bg = pygame.image.load("City.png")
#py.blit(bg, (0, 0))

#pygame.quit()
