"""
Level Functions
"""

from ..Components import Info, Player
from .. import Setup, Tools
from .. import Constant as Con 
import pygame

class Level:
    def __init__(self):
        self.finished = False
        self.next = None 
        self.setup_background()
        self.setup_player()

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
        self.player = Player.Player("Mario")
        self.player.rect.x = 300
        self.player.rect.y = 498

    def update(self,surface,keys):
        self.player.update(keys)
        self.update_player_position()
        self.draw(surface)

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def create_label(self,label,size = 18,width_scale = 1.25,height_scale = 1):
        font = pygame.font.Font(Con.FONT,size) 
        label_img = font.render(label,1,(255,255,255))
        return label_img 

    def draw(self,surface):
        surface.blit(self.background,self.viewport)
        surface.blit(self.create_label("Ahri and Dva are my waifus!!!"),(170,280))

        surface.blit(self.player.image,self.player.rect)
