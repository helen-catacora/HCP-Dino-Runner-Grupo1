import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART,SHIELD

class Small_heart(Sprite):
    def __init__(self,lifes=0):
        
        image = HEART
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 100
        self.image_rect.y = 9
        self.image2 = image
        self.image2_rect = self.image.get_rect()
        self.image2_rect.x = 150
        self.image2_rect.y = 9
        self.image3= image
        self.image3_rect = self.image.get_rect()
        self.image3_rect.x = 200
        self.image3_rect.y = 9
        pass

    def update(self):
        pass
    
    def draw(self, screen,lives=2):
        if lives == 3:
            screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
            screen.blit(self.image2,(self.image2_rect.x,self.image2_rect.y))
            screen.blit(self.image3,(self.image3_rect.x,self.image3_rect.y))
        elif lives == 2:
            screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
            screen.blit(self.image2,(self.image2_rect.x,self.image2_rect.y))
        elif lives == 1:
            screen.blit(self.image,(self.image_rect.x,self.image_rect.y))