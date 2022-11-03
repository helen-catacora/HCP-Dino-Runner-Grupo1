import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART

class Small_heart(Sprite):
    def __init__(self):
        self.image=HEART
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 10
        self.image_rect.y = 9
        pass

    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
