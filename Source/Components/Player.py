"""
The player aka mario bros
"""

import pygame 
from .. import Tools, Setup
from .. import Constant as Con 

class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name 
        self.setup_states()
        self.setup_velocity()
        self.setup_timer()
        self.load_images()
        # self.frame_index = 0
        # self.image = self.frames[self.frame_index]
        # self.rect = self.image.get_rect()

    def setup_states(self):
        self.face_right = True 
        self.dead = False 
        self.big = False 

    def setup_velocity(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timer(self):
        self.walking_timer = 0
        self.transition_time = 0

    def load_images(self):
        sheet = Setup.GRAPHICS["Mario_and_Luigi"]

        self.right_frames = []
        self.left_frames = []
        self.up_frames = []
        self.down_frames = []
        self.stop_frames = []

        frame_rects = [
            (80,34,15,15),
            (97,34,15,15),
            (114,34,15,15),
            (131,34,15,15)
        ]

        for frame_rect in frame_rects:
            right_img = Tools.get_image(sheet,*frame_rect,(0,0,0),Con.PLAYER_MULTI)
            left_img = pygame.transform.flip(right_img,True,False)
            up_img = pygame.transform.rotate(right_img,90)
            down_img = pygame.transform.rotate(right_img,-90)
            stop_img = Tools.get_image(sheet,80,34,15,15,(0,0,0),Con.PLAYER_MULTI)

            self.right_frames.append(right_img)
            self.left_frames.append(left_img)
            self.up_frames.append(up_img)
            self.down_frames.append(down_img)
            self.stop_frames.append(stop_img)

        self.frames = []
        self.frames.append(Tools.get_image(sheet,80,34,15,15,(0,0,0),Con.PLAYER_MULTI))

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self,keys):
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
            self.face_right = True
        elif keys[pygame.K_LEFT]:
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames
            self.face_right = False 
        elif keys[pygame.K_UP]:
            self.x_vel = 0
            self.y_vel = -5
            self.frames = self.up_frames
        elif keys[pygame.K_DOWN]:
            self.x_vel = 0
            self.y_vel = 5
            self.frames = self.down_frames
        else: 
            self.x_vel = 0
            self.y_vel = 0
            self.frames = self.stop_frames

        if self.current_time - self.walking_timer > 100:
            self.walking_time = self.current_time 
            self.frame_index += 1
            self.frame_index %= 4
        self.image = self.frames[self.frame_index]
