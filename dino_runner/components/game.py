import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.components.dinosuar import Dinosaur
from dino_runner.components.nube import NubeHandler
from dino_runner.components.heart import Small_heart
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils import text_utils
from dino_runner.components.obstacles.bird import Bird

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE) 
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.dinosaur = Dinosaur()
        self.nube = NubeHandler()
        #self.bird = Bird()
        self.small_heart = Small_heart() 
        self.obstacle_handler = ObstacleHandler()
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 1
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        dino_event = pygame.key.get_pressed()
        self.dinosaur.update(dino_event)
        self.nube.update(self.game_speed)
        self.small_heart.update()
        self.obstacle_handler.update(self.game_speed,self.dinosaur)
        #self.bird.update(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.nube.draw(self.screen)
        self.small_heart.draw(self.screen)
        self.obstacle_handler.draw(self.screen) 
        self.draw_score()
        #self.bird.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
       

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.points += 1
        message = "Points: "+ str(self.points)
        points_text , points_rect = text_utils.get_text_element(message,1000,50)
        self.screen.blit(points_text,points_rect)
        
