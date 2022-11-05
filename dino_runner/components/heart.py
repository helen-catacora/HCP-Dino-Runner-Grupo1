import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART

class Small_heart(Sprite):
    def __init__(self,lifes=0):
        
        image = HEART
        self.images = [image,image,image]
        self.x = 100
        self.y = 9

    def update(self):
        pass
    
    def draw(self, screen,lives=2):
        x = 0
        for i in range (lives):
            x += 30
            self.image = self.images[i]
            self.image_rect = self.image.get_rect()
            self.image_rect.x = self.x + x
            self.image_rect.y = self.y
            screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
        
