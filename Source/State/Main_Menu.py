"""
Main menu set up
"""

import pygame
from .. import Setup
from .. import Tools 
from .. import Constant as Con 
from ..Components import Info

class MainMenu: 
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor() 
        self.info = Info.Info("Main_Menu")
        self.finished = False
        self.next = "Load_Screen"

    def setup_background(self):
        self.background = Setup.GRAPHICS['World_1-1']
        self.background_rect = self.background.get_rect() 
        self.background = pygame.transform.scale(self.background,
                                                (int(self.background_rect.width * Con.BG_MULTI),
                                                 int(self.background_rect.height * Con.BG_MULTI)))
        self.viewport = Setup.SCREEN.get_rect()
        self.caption = Tools.get_image(Setup.GRAPHICS['Title_Screen'],
                                       1,60,176,88,(225,0,220),Con.BG_MULTI)

    def setup_player(self):
        self.player_img = Tools.get_image(Setup.GRAPHICS['Mario_and_Luigi'],
                                         80,34,16,16,(0,0,0),Con.PLAYER_MULTI)

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = Tools.get_image(Setup.GRAPHICS['Items_Objects_and_NPCs'],
                                            23,160,9,8,(0,0,0),Con.BG_MULTI) 
        rect = self.cursor.image.get_rect()
        rect.x,rect.y = (220,357)
        self.cursor.rect = rect
        self.cursor.state = "1P"

    def update_cursor(self,keys):
        if keys[pygame.K_UP]:
            self.cursor.state = "1P"
            self.cursor.rect.y = 357
        elif keys[pygame.K_DOWN]:
            self.cursor.state = "2P"
            self.cursor.rect.y = 402
        elif keys[pygame.K_RETURN]:
            if self.cursor.state == "1P":
                self.finished = True 
            elif self.cursor.state == "2P":
                self.finished = True  

    def update(self,surface,keys):
        self.update_cursor(keys)

        surface.blit(self.background,self.viewport)
        surface.blit(self.caption,(165,100))
        surface.blit(self.player_img,(110,498))
        surface.blit(self.cursor.image,self.cursor.rect)

        self.info.update()
        self.info.draw(surface)