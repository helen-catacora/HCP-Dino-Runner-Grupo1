import random
from dino_runner.components.obstacles.obstacle import Obtacles

class Cactu(Obtacles):
    def __init__(self, images,pos_y=310):
        index = random.randint(0,2)
        super().__init__(images, index)
        self.image_rect.y = pos_y

    pass