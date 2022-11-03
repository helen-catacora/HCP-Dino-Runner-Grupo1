
from dino_runner.utils.constants import BIRD
from dino_runner.utils.constants import SCREEN_WIDTH

class Bird():
    MAX_STEP = 10
    INITIAL = 0

    def __init__(self, x_post = SCREEN_WIDTH):
        self.image = BIRD[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.y = 250
        self.image_rect.x = x_post
        self.step = self.INITIAL
        self.bird_fly = True
    
    def update(self, speed):
        self.image_rect.x -= speed

        if self.bird_fly:
            self.fly()

        if self.step > self.MAX_STEP:
            self.step = self.INITIAL
        

    def fly(self):
        self.image = BIRD[0]  if self.step <= 5 else BIRD[1]
        self.step += 1

    def draw(self,screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))


    
