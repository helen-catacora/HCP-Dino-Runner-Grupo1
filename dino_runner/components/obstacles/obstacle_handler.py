from dino_runner.utils.constants import SMALL_CACTUS,BIRD,LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactu
from dino_runner.components.obstacles.bird import Bird
import pygame
import random
from dino_runner.components.obstacles.bird import Bird
class ObstacleHandler():
    def __init__(self):
        self.obstacles = []
        
    def update(self,speed, dino):
        if len(self.obstacles) == 0:
            auxiliar = random.randint(0,3)
            if auxiliar == 0:
                self.obstacles.append(Cactu(SMALL_CACTUS,320))
            elif auxiliar ==1:
                self.obstacles.append(Cactu(LARGE_CACTUS,300))
            elif auxiliar == 2:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            obstacle.update(speed)

            if dino.image_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(300)
                self.obstacles.pop()

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()


    def draw (self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

