"""
Game setup functions
"""

import pygame 
from . import Constant as Con 
from . import Tools 

pygame.init() 
SCREEN = pygame.display.set_mode(Con.SCREEN_SIZE)

GRAPHICS = Tools.load_graphics("Resources/Graphics")