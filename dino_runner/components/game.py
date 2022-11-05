import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEAD,DINO

from dino_runner.components.dinosuar import Dinosaur
from dino_runner.components.nube import NubeHandler
from dino_runner.components.heart import Small_heart
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.utils import text_utils
from dino_runner.components.obstacles.bird import Bird

class Game:
    MAX_LIFES = 3
    INITIAL_SPEED = 10

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE) 
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        self.dinosaur = Dinosaur()
        self.nube = NubeHandler()
        #self.bird = Bird()
        self.small_heart = Small_heart() 
        self.obstacle_handler = ObstacleHandler()
        self.game_speed = self.INITIAL_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.lives = self.MAX_LIFES
        self.image_game = DEAD
        self.image_game_rect = self.image_game.get_rect()
        self.image_game_rect.x = 540
        self.image_game_rect.y = 100
        self.image2_game = DINO
        self.image2_game_rect = self.image2_game.get_rect()
        self.image2_game_rect.x = 500
        self.image2_game_rect.y = 160
        self.day = 0
        self.sun = (255, 255, 255)
        self.moon = (107, 114, 142)

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
        
    
    def run(self):
        # Game loop: events - update - draw
        self.reset_attributes()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def reset_attributes(self):
        self.playing = True
        self.dinosaur = Dinosaur()
        self.obstacle_handler = ObstacleHandler()
        self.points = 0
        self.lives = self.MAX_LIFES
        self.game_speed = self.INITIAL_SPEED
        self.day = 0
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        dino_event = pygame.key.get_pressed()
        self.dinosaur.update(dino_event)
        self.nube.update(self.game_speed)
        self.small_heart.update()
        self.update_score()
        self.obstacle_handler.update(self)
        
        

    
        if self.lives == 0 :
            self.playing = False
            self.running = True
            self.execute()

    def draw(self):
        white = (255, 255, 255)
        black = (0,0,0)
        self.clock.tick(FPS)
        #self.points % 100 == 0 and self.points % 300 != 0
        if (self.points>=300 and self.points % 300 == 0) or self.day == 1:
            self.day = 1
            self.screen.fill(self.moon)
            if self.points % 100 == 0 and self.points % 300 != 0:
                self.day = 0
                self.screen.fill(self.moon)
        if self.day == 0:
            self.screen.fill(self.sun)
        #self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.nube.draw(self.screen)
        self.small_heart.draw(self.screen,lives=self.lives)
        self.obstacle_handler.draw(self.screen) 
        self.draw_score()
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
        if self.day == 0:
            text_color = (0,0,0)
        else:
            text_color = (255,255,255)
            pass
        points_text , points_rect = text_utils.get_text_element(message,1000,50,color= text_color )
        self.screen.blit(points_text,points_rect)
        message_life = "   LIVES = "
        points_text , points_rect = text_utils.get_text_element(message_life,50,20,25, color= text_color )
        self.screen.blit(points_text,points_rect)


    def update_score(self):
        if self.points % 100 == 0:
            self.game_speed +=2

    def show_menu(self):
        self.running = True

        background_color = (232, 223, 202)
        self.screen.fill(background_color)

        self.show_menu_options()

        pygame.display.update()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.run()
        #pygame.display.update()

    def show_menu_options(self):
        text_color = (0,0,0)
        if self.points > 0:
            text,text_rect = text_utils.get_text_element("GAME OVER",550,250,font_size=60 , color=text_color)
            text2,text_rect2 = text_utils.get_text_element("Press any key to start :D",550,400,font_size=40 , color=text_color)
            self.screen.blit(text,text_rect)
            self.screen.blit(text2,text_rect2)
            self.screen.blit(self.image_game,(self.image_game_rect.x,self.image_game_rect.y))
        else:
            self.screen.blit(self.image2_game,(self.image2_game_rect.x,self.image2_game_rect.y))
            text,text_rect = text_utils.get_text_element("Press any key to start :D",font_size=40 , color=text_color)   
            self.screen.blit(text,text_rect)
    
