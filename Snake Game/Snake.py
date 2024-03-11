import pygame
import random
from pygame.math import Vector2

pygame.init()

#Variables
FPS = 60
CELLS_NUMBER = 20
CELLS_SIZE= 40

SCREEN_UPDATE = pygame.USEREVENT

class Button:
    def __init__(self, app, x_pos, y_pos, text_input):
        self.font = pygame.font.Font("Snake Game/SnakeHoliday.otf", 45)
        self.app = app
        self.image = pygame.image.load("Snake Game/button.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 150))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = self.font.render(self.text_input, False, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        
    def update_image(self):
        app.screen.blit(self.image, self.rect)
        app.screen.blit(self.text, self.text_rect)
        
    def check_input(self, position_mouse):
        if position_mouse[0] in range(self.rect.left, self.rect.right) and position_mouse[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def change_color(self, position_mouse):
        if position_mouse[0] in range(self.rect.left, self.rect.right) and position_mouse[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, "Black")
        else:
            self.text = self.font.render(self.text_input, True, "White")


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
    def __init__(self,app, color="Original"):
        self.app = app
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
        if color == "Original":
            folder_path = "Snake Game/Graphics/Original/"
        elif color == "Red":
            folder_path = "Snake Game/Graphics/Red/"
        elif color == "DarkGreen":
            folder_path = "Snake Game/Graphics/DarkGreen/"
        
        self.tail_up = pygame.image.load(folder_path + "tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(folder_path + "tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(folder_path + "tail_right.png").convert_alpha()
        self.tail_left =  pygame.image.load(folder_path + "tail_left.png").convert_alpha()
        
        self.head_down = pygame.image.load(folder_path + "head_down.png").convert_alpha()
        self.head_up = pygame.image.load(folder_path + "head_up.png").convert_alpha()
        self.head_right = pygame.image.load(folder_path + "head_right.png").convert_alpha()
        self.head_left = pygame.image.load(folder_path + "head_left.png").convert_alpha()
        
        self.body_topleft = pygame.image.load(folder_path + "body_topleft.png").convert_alpha()
        self.body_topright = pygame.image.load(folder_path + "body_topright.png").convert_alpha()
        self.body_bottomleft = pygame.image.load(folder_path + "body_bottomleft.png").convert_alpha()
        self.body_bottomright = pygame.image.load(folder_path + "body_bottomright.png").convert_alpha()
        
        self.body_horizontal = pygame.image.load(folder_path + "body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load(folder_path + "body_vertical.png").convert_alpha()
        
        self.eat_sound = pygame.mixer.Sound("Snake Game/eating_sound2.mp3")
        
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
        
    def play_eat_sound(self):
        self.eat_sound.play()

class Main:
    def __init__(self, app, color = "Original"):
        self.snake = Snake(app, color)
        self.fruit = Fruit(app)
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
        
    def draw_elements(self):
        self.draw_board()
        self.draw_score()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.new_random_position()
            self.snake.add_cell()
            self.snake.play_eat_sound()
        
        for cell in self.snake.body[1:]:
            if cell == self.fruit.pos:
                self.fruit.new_random_position()
            
    def check_fail(self):
        #Check if snake is out of the screen
        if not 0 <= self.snake.body[0].x < CELLS_NUMBER or not 0 <= self.snake.body[0].y < CELLS_NUMBER:
            self.game_over()
            
        #check if snake hits itself
        for cell in self.snake.body[1:]:
            if cell == self.snake.body[0]:
                self.game_over()
            
    def game_over(self):
        game_over_menu= True
        game_over_font = pygame.font.Font("Snake Game/SnakeHoliday.otf", 55)
        while game_over_menu:
            MOUSE_POS = pygame.mouse.get_pos()
            
            
            game_over_text = "Perdiste"
            score_text = f"tu puntacion fue: {str((len(self.snake.body) - 3))}"
            
            game_over_surface = game_over_font.render(game_over_text, True, "Black")
            score_surface = game_over_font.render(score_text, True, "Black")
            
            game_over_x = 400
            game_over_y = 50
            score_x = 400
            score_y = 150
            
            game_over_rect = game_over_surface.get_rect(center = (game_over_x,game_over_y))
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            
            app.screen.blit(game_over_surface, game_over_rect)
            app.screen.blit(score_surface, score_rect)
            
            
            RETRY_BUTTON = Button(self, 400, 300, "Reintentar")
            SUMBIT_BUTTON = Button(self, 400, 500, "Enviar Puntuacion")
            QUIT_BUTTON = Button(self, 400, 700, "Salir")
            
            for button in [RETRY_BUTTON, SUMBIT_BUTTON, QUIT_BUTTON]:
                button.change_color(MOUSE_POS)
                button.update_image()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RETRY_BUTTON.check_input(MOUSE_POS):
                            self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
                            self.snake.direction = Vector2(1,0)
                            game_over_menu = False
                            
                    if SUMBIT_BUTTON.check_input(MOUSE_POS):
                        pass
                    if QUIT_BUTTON.check_input(MOUSE_POS):
                        pygame.quit()
                        exit()
            

            pygame.display.update()
            
        
    def draw_board(self):
        grass_color = (167,209,61)
        
        for i in range(CELLS_NUMBER):
            if i % 2 == 0:
                for j in range(CELLS_NUMBER):
                    if j % 2 == 0:
                        board_rect = pygame.Rect(i* CELLS_SIZE, j * CELLS_SIZE, CELLS_SIZE, CELLS_SIZE)
                        pygame.draw.rect(app.screen, grass_color, board_rect)
            else:
                for j in range(CELLS_NUMBER):
                    if j % 2 != 0:
                        board_rect = pygame.Rect(i* CELLS_SIZE, j * CELLS_SIZE, CELLS_SIZE, CELLS_SIZE)
                        pygame.draw.rect(app.screen, grass_color, board_rect)
                        
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = app.font.render(score_text,True,"Black")
        score_x = int(CELLS_NUMBER * CELLS_SIZE - 60)
        score_y = int(CELLS_NUMBER * CELLS_SIZE - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        app.screen.blit(score_surface, score_rect)
                

class App:
    def __init__(self):
        self.screen =  pygame.display.set_mode((CELLS_NUMBER * CELLS_SIZE, CELLS_NUMBER * CELLS_SIZE))
        self.clock = pygame.time.Clock()
        #Aca
        self.main_game = Main(self)
        self.apple = pygame.image.load("Snake Game/apple.png").convert_alpha()
        self.font = pygame.font.Font("Snake Game/SnakeHoliday.otf", 25)
        
    def play_game(self):
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
        
        
    def options_game(self):
        menu = True
        while menu:
            self.screen.fill((180, 230, 80))
            MOUSE_POS = pygame.mouse.get_pos()
            
            ORIGINAL_BUTTON = Button(self, 400, 100, "Original")
            RED_BUTTON = Button(self, 400, 300, "Rojo")
            BLACK_BUTTON = Button(self, 400, 500, "Negro")
            GREEN_BUTTON = Button(self, 400, 700, "Verde Oscuro")
            
            
            for button in [ORIGINAL_BUTTON, RED_BUTTON, BLACK_BUTTON, GREEN_BUTTON]:
                button.change_color(MOUSE_POS)
                button.update_image()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ORIGINAL_BUTTON.check_input(MOUSE_POS):
                        self.main_game = Main(self, "Original")
                        menu = False
                    if RED_BUTTON.check_input(MOUSE_POS):
                        self.main_game = Main(self, "Red")
                        menu = False
                    if BLACK_BUTTON.check_input(MOUSE_POS):
                        self.main_game = Main(self, "Black")
                        menu = False
                    if GREEN_BUTTON.check_input(MOUSE_POS):
                        self.main_game = Main(self, "DarkGreen")
                        menu = False
            

            pygame.display.update()
            
        
    def run(self):
        while True:
            self.screen.fill((180, 230, 80))
            MOUSE_POS = pygame.mouse.get_pos()
            
            PLAY_BUTTON = Button(self, 400, 200, "Jugar")
            OPTIONS_BUTTON = Button(self, 400, 400, "Opciones")
            QUIT_BUTTON = Button(self, 400, 600, "Salir")
            
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.change_color(MOUSE_POS)
                button.update_image()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.check_input(MOUSE_POS):
                        self.play_game()
                    if OPTIONS_BUTTON.check_input(MOUSE_POS):
                        self.options_game()
                    if QUIT_BUTTON.check_input(MOUSE_POS):
                        pygame.quit()
                        exit()
            

            pygame.display.update()

        
if __name__ == "__main__":
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 140)
    app = App()
    app.run()
