"""
Collecting coins in the game
"""

import pygame 
from .. import Tools, Setup
from .. import Constant as Con 

class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frame_index = 0
        frame_rects = [(1,160,4,7),(9,160,4,7),(17,160,4,7),(9,160,4,7)]
        self.load_frames(frame_rects)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 53
        self.timer = 0

    def load_frames(self,frame_rects):
        sheet = Setup.GRAPHICS["Items_Objects_and_NPCs"]
        for frame_rect in frame_rects:
            self.frames.append(Tools.get_image(sheet,*frame_rect,(0,0,0),Con.BG_MULTI))

    def update(self):
        self.current_time = pygame.time.get_ticks()
        frame_durations = [375,125,125,125]

        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= 4
            self.timer = self.current_time

        self.image = self.frames[self.frame_index]