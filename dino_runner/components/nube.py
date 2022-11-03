
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD
import random
from dino_runner.utils.constants import SCREEN_WIDTH

class Nube(Sprite):
    def __init__(self,x_post = SCREEN_WIDTH):
        self.imagec=CLOUD
        self.imagec_rect = self.imagec.get_rect()
        self.imagec_rect.y = random.randint(9,200)
        self.imagec_rect.x = x_post
        pass


    def update(self,speed):
        self.imagec_rect.x -= speed
    
    def draw(self, screen):
        screen.blit(self.imagec,(self.imagec_rect.x,self.imagec_rect.y))


class NubeHandler():
    def __init__(self):
        self.nubes = []

    def update(self,speed):
        if len(self.nubes) == 0:
            self.nubes.append(Nube())
        
        for nube in self.nubes:
            nube.update(speed)

            if nube.imagec_rect.x < -nube.imagec_rect.width:
                self.nubes.pop()

    def draw(self,screen):
        for nube in self.nubes:
            nube.draw(screen)
