"""
Game info
"""

import pygame 
from .. import Constant as Con 
from . import Coin

pygame.font.init()

class Info:
    def __init__(self,state):
        self.state = state 
        self.create_state_labels() 
        self.create_info_labels() 
        self.flash_coin = Coin.FlashingCoin()

    def create_state_labels(self):
        self.state_labels = []
        if self.state == "Main_Menu":
             self.state_labels.append((self.create_label("1 PLAYER GAME"),(272,360)))
             self.state_labels.append((self.create_label("2 PLAYER GAME"),(272,405)))
             self.state_labels.append((self.create_label("TOP - "),(280,465)))
             self.state_labels.append((self.create_label("000000"),(390,465)))

    def create_info_labels(self):
        self.info_labels = []
        self.info_labels.append((self.create_label("MARIO"),(75,30)))
        self.info_labels.append((self.create_label("WORLD"),(450,30)))
        self.info_labels.append((self.create_label("TIME"),(625,30)))
        self.info_labels.append((self.create_label("000000"),(75,55)))
        self.info_labels.append((self.create_label("x00"),(300,55)))
        self.info_labels.append((self.create_label("1 - 1"),(450,55)))

    def create_label(self,label,size = 18,width_scale = 1.25,height_scale = 1):
        font = pygame.font.Font(Con.FONT,size) 
        label_img = font.render(label,1,(255,255,255))
        return label_img 

    def update(self):
        self.flash_coin.update() 

    def draw(self,surface):
        # surface.blit(self.create_label("Ahri and Dva are mine!!!"),(150,1)) 

        for label in self.state_labels:
            surface.blit(label[0],label[1])

        for label in self.info_labels:
            surface.blit(label[0],label[1])

        surface.blit(self.flash_coin.image,self.flash_coin.rect)