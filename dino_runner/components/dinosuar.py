
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING,JUMPING,DUCKING


class Dinosaur(Sprite):

    DINO_X_POS = 50
    DINO_Y_POS = 300
    INTIAL_STEP = 0
    MAX_STEP = 20
    ACELERATION = 4
    INTIAL_VELOCITY = 8
    REDUCE_VELOCITY = 0.9



    def __init__(self):
        self.image = RUNNING[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step = self.INTIAL_STEP
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False
        self.dino_velocity = self.INTIAL_VELOCITY



    def update(self, dino_event): 
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()

        if dino_event[pygame.K_UP]:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
                
        elif dino_event[pygame.K_DOWN]:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step > self.MAX_STEP:
            self.step = self.INTIAL_STEP

    def run(self):
        self.image = RUNNING[0]  if self.step <= 10 else RUNNING[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS
        self.step += 1

    def duck(self):
        self.image = DUCKING[0]  if self.step <= 10 else DUCKING[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.DINO_X_POS
        self.image_rect.y = self.DINO_Y_POS + 35
        self.step += 1
        pass

    def jump(self):
    
        self.image= JUMPING 
        if self.dino_jump:
            self.image_rect.y -= self.dino_velocity * self.ACELERATION
            self.dino_velocity -= self.REDUCE_VELOCITY
        if self.dino_velocity < -self.INTIAL_VELOCITY:
            self.image_rect.y = self.DINO_Y_POS
            self.dino_jump = False
            self.dino_velocity = self.INTIAL_VELOCITY
            self.dino_run = True
        



        '''
        prueba 2
        self.image= JUMPING 
        if self.image_rect.y < 100:
            self.image_rect.y += 10
        elif self.dino_jump:
            self.image_rect.y -= 10
        if self.image_rect.y == self.DINO_Y_POS:
            self.dino_jump = False
            self.dino_run = True


        prueba1
        self.image = JUMPING
        if self.dino_jump:
            self.image_rect.y -= 20
            print("1. ",self.image_rect.y)
        if self.image_rect.y < 100:
            while self.image_rect.y != self.DINO_Y_POS:
                self.image_rect.y += 20
            self.dino_jump = False
            self.dino_run = True'''

        


    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
    

