# -*- coding: utf-8 -*-

#Game
#03.03.2012 10:49:10
#Von: Isaak Lim & Jonathan Wendler
#äöü

import pygame,sys,os
from pygame.locals import *
from sys import exit

pygame.init()
windos = pygame.display.set_mode((468, 60))
pygame.display.set_caption('Game')
screen = pygame.display.get_surface()

pygame.display.flip() 
##PROZEDUREN##

#--Menu--#
def Menu():
    print 'GAME'
#--Menu--#

#--input(event)--#
def input(events):
    for event in events:
        if event.type == QUIT:
            exit()
        else:
            print event
#--input(event)--#

##PROZEDUREN##
Menu

while True:
    input(pygame.event.get())
