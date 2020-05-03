"""
Screen loading functions
"""

from ..Components import Info
import pygame

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = "Level"
        self.timer = 0

    def update(self,surface,keys):
        self.draw(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True 
            self.timer = 0

    def draw(self,surface):
        surface.fill((0,0,0))