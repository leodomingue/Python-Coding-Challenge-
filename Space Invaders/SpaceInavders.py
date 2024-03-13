import pygame
import random
from player import Player

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
        player_sprite = Player((WIDTH/2,HEIGHT), WIDTH)
        self.player = pygame.sprite.GroupSingle(player_sprite)
    
    def run_game(self):
        self.player.update()
        self.player.draw(app.screen)

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
