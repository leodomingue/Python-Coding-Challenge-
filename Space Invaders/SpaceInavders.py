import pygame
import random
from player import Player
import obstacle

#VARIABLE
WIDTH = 800
HEIGHT = 800
FPS = 60

#COLORS
BLACK = (0,0,0)

#Class Logic
class Game:
    def __init__(self, app):
        self.app = app
        
        #PLayer setup
        player_sprite = Player((WIDTH/2,HEIGHT), WIDTH, HEIGHT)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.block = pygame.sprite.Group()
        self.obtacle_amount = 4
        self.obstacle_x_positions = [num * (WIDTH/ self.obtacle_amount) for num in range(self.obtacle_amount)]
        self.create_multiple_obstacle(WIDTH/20, 650, *self.obstacle_x_positions)
        
    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (240, 79, 80), x, y)
                    self.block.add(block)
                    
    def create_multiple_obstacle(self, x_start, y_start, *offset):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)
        
    
    def run_game(self):
        self.player.update()
        
        self.player.sprite.shoots.draw(app.screen)
        self.player.draw(app.screen)
        self.block.draw(app.screen)

class App:
    def __init__(self):
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game = Game(self)
        
        
    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
                    
            self.screen.fill(BLACK)
            self.game.run_game()
                
            pygame.display.update()
            
        



if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()
