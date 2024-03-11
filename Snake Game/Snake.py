import pygame
import random
from pygame.math import Vector2

#Variables
FPS = 60
CELLS_NUMBER = 20
CELLS_SIZE= 40

SCREEN_UPDATE = pygame.USEREVENT


class Fruit:
    def __init__(self,app):
        self.app = app
        
        self.new_random_position()
        
    #Create figure
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELLS_SIZE) ,int(self.pos.y *CELLS_SIZE) ,CELLS_SIZE ,CELLS_SIZE)
        pygame.draw.rect(app.screen,"Red",fruit_rect)
        
    def new_random_position(self):
        self.x = random.randint(0,CELLS_NUMBER - 1)
        self.y = random.randint(0,CELLS_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        
        
class Snake:
    def __init__(self,app):
        self.app = app
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
    #Create Snake
    def draw_snake(self):
        for cell in self.body:
            x_pos = cell.x
            y_pos = cell.y
            cell_rect = pygame.Rect(int(x_pos * CELLS_SIZE), int(y_pos * CELLS_SIZE), CELLS_SIZE, CELLS_SIZE)
            pygame.draw.rect(app.screen, "Blue", cell_rect)
            
    #Moving Snake
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
        
    def add_cell(self):
        self.new_block = True
        

class Main:
    def __init__(self, app):
        self.snake = Snake(app)
        self.fruit = Fruit(app)
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.new_random_position()
            self.snake.add_cell()
            
    def check_fail(self):
        #Check if snake is out of the screen
        if not 0 <= self.snake.body[0].x < CELLS_NUMBER or not 0 <= self.snake.body[0].y < CELLS_NUMBER:
            self.game_over()
            
        #check if snake hits itself
        for cell in self.snake.body[1:]:
            if cell == self.snake.body[0]:
                print("b")
            
    def game_over(self):
        print("nada")

class App:
    def __init__(self):
        self.screen =  pygame.display.set_mode((CELLS_NUMBER * CELLS_SIZE, CELLS_NUMBER * CELLS_SIZE))
        self.clock = pygame.time.Clock()
        self.main_game = Main(self)
        
        
    def run(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == SCREEN_UPDATE:
                    self.main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.main_game.snake.direction.y != 1:
                            self.main_game.snake.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN:
                        if self.main_game.snake.direction.y != -1:
                            self.main_game.snake.direction = Vector2(0, 1)
                    if event.key == pygame.K_RIGHT:
                        if self.main_game.snake.direction.x != -1:
                            self.main_game.snake.direction = Vector2(1, 0)
                    if event.key == pygame.K_LEFT:
                        if self.main_game.snake.direction.x != 1:
                         self.main_game.snake.direction = Vector2(-1, 0)
                    

            self.screen.fill((180, 230, 80))
            self.main_game.draw_elements()
            
            pygame.display.update()

        
if __name__ == "__main__":
    pygame.init()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    app = App()
    app.run()
