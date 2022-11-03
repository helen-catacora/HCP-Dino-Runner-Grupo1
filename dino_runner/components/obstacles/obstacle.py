from turtle import speed
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obtacles(Sprite):
    def __init__(self, images , index, x_post = SCREEN_WIDTH):
        self.image = images[index]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_post

    def update(self,speed):
        self.image_rect.x -= speed

    def draw(self,screen):
        screen.blit(self.image,self.image_rect)

