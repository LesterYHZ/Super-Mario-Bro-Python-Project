"""
Functions of various tools
"""

import pygame 
import random
import os 

class Game:
    def __init__(self):
        # Initialize window
        self.screen = pygame.display.get_surface() 
        self.clock = pygame.time.Clock()

    def run(self,GRAPHICS):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit() 
                elif event.type == pygame.KEYDOWN:
                    self.key = pygame.key.get_pressed() 
                elif event.type == pygame.KEYUP:
                    self.key = pygame.key.get_pressed() 

            # screen update toy code
            self.screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

            img = get_image(GRAPHICS['Mario_and_Luigi'],80,34,16,16,(0,0,0),random.randint(0,15))
            self.screen.blit(img,(300,300))
            pygame.display.update()
            self.clock.tick(30) # 30 FPS 


def load_graphics(path, accept = ('.jpg','.png','.bmp','.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img 
    return graphics

def get_image(sheet, x, y, width, height, colorkey, scale):
    """
    " sheet: 图片
    " x,y: 图片左上角坐标
    " width,height: 图片宽高
    " colorkey: 抠图底色
    " scale: 放大缩小比例
    """
    img = pygame.Surface((width,height))
    img.blit(sheet, (0,0),(x,y,width,height))
    img.set_colorkey(colorkey)
    img = pygame.transform.scale(img, (int(width*scale),int(height*scale)))
    return img 
