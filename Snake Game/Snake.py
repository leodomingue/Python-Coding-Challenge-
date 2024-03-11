import pygame
import random
from pygame.math import Vector2

pygame.init()

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
        fruit_rect = pygame.Rect(int(self.pos.x * CELLS_SIZE) ,int(self.pos.y *CELLS_SIZE) ,CELLS_SIZE,CELLS_SIZE)
        app.screen.blit(app.apple, fruit_rect)
        
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
        
        self.tail_up = pygame.image.load("Snake Game/Graphics/Original/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("Snake Game/Graphics/Original/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("Snake Game/Graphics/Original/tail_right.png").convert_alpha()
        self.tail_left =  pygame.image.load("Snake Game/Graphics/Original/tail_left.png").convert_alpha()
        
        self.head_down = pygame.image.load("Snake Game/Graphics/Original/head_down.png").convert_alpha()
        self.head_up = pygame.image.load("Snake Game/Graphics/Original/head_up.png").convert_alpha()
        self.head_right = pygame.image.load("Snake Game/Graphics/Original/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("Snake Game/Graphics/Original/head_left.png").convert_alpha()
        
        self.body_topleft = pygame.image.load("Snake Game/Graphics/Original/body_topleft.png").convert_alpha()
        self.body_topright = pygame.image.load("Snake Game/Graphics/Original/body_topright.png").convert_alpha()
        self.body_bottomleft = pygame.image.load("Snake Game/Graphics/Original/body_bottomleft.png").convert_alpha()
        self.body_bottomright = pygame.image.load("Snake Game/Graphics/Original/body_bottomright.png").convert_alpha()
        
        self.body_horizontal = pygame.image.load("Snake Game/Graphics/Original/body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load("Snake Game/Graphics/Original/body_vertical.png").convert_alpha()
        
        self.head = self.head_right
        self.tail = self.tail_right
        
    #Create Snake
    def draw_snake(self):
        self.update_head()
        self.update_tail()
        
        for index, cell in enumerate(self.body):
            #Rect for the positioning
            x_pos = int(cell.x * CELLS_SIZE)
            y_pos = int(cell.y * CELLS_SIZE)
            cell_rect = pygame.Rect(x_pos, y_pos, CELLS_SIZE, CELLS_SIZE)
            
            #direction of the head
            if index == 0:
                app.screen.blit(self.head, cell_rect)
            #Direction of the Tail
            elif index == len(self.body) -1:
                app.screen.blit(self.tail, cell_rect)    
            else:
                previous_cell = self.body[index + 1] - cell
                next_cell = self.body[index - 1] - cell
                
                if previous_cell.x == next_cell.x:
                    app.screen.blit(self.body_vertical, cell_rect)
                if previous_cell.y == next_cell.y:
                    app.screen.blit(self.body_horizontal, cell_rect)
                else:
                    if previous_cell.x == -1 and next_cell.y == -1 or previous_cell.y == -1 and next_cell.x == -1:
                        app.screen.blit(self.body_topleft, cell_rect)
                    elif previous_cell.x == -1 and next_cell.y == 1 or previous_cell.y == 1 and next_cell.x == -1:
                        app.screen.blit(self.body_bottomleft, cell_rect)
                    elif previous_cell.x == 1 and  next_cell.y == -1 or previous_cell.y == -1 and next_cell.x == 1:
                        app.screen.blit(self.body_topright, cell_rect)
                    elif previous_cell.x == 1 and next_cell.y == 1 or previous_cell.y == 1 and next_cell.x == 1:
                        app.screen.blit(self.body_bottomright, cell_rect)
        
        
    def update_head(self):
        relation = self.body[1] - self.body[0]
        if relation == Vector2(1,0):
            self.head = self.head_left
        elif relation == Vector2(-1, 0):
            self.head = self.head_right
        elif relation == Vector2(0, 1):
            self.head = self.head_up
        elif relation == Vector2(0, -1):
            self.head = self.head_down
            
    def update_tail(self):
        relation = self.body[len(self.body) -2] - self.body[len(self.body) -1]
        if relation == Vector2(1,0):
            self.tail = self.tail_left
        elif relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif relation == Vector2(0, -1):
            self.tail = self.tail_down
            
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
        self.apple = pygame.image.load("Snake Game/apple.png").convert_alpha()
        
        
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
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    app = App()
    app.run()
