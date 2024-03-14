import pygame
import random
from player import Player
import obstacle
from alien import Alien, Extra
from bullet import Bullet

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
        
        #Alien Setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
        self.alien_direction = 1
        self.alien_shoots = pygame.sprite.Group()
        
        #Alien Extra
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = random.randint(400, 800)
        
    def extra_alien_time(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(random.choice(["right","left"]), WIDTH))
            self.extra_spawn_time = random.randint(400, 800)
        
    def alien_postion_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= WIDTH:
                self.alien_direction =  -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction =  1
                self.alien_move_down(2)
                
    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance
                
    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = random.choice(self.aliens.sprites())
            shoot_sprite = Bullet(random_alien.rect.center, -6, WIDTH)
            self.alien_shoots.add(shoot_sprite)
            
        
        
    def alien_setup(self, rows, cols, x_distance = 90, y_distance = 50, x_offset = 70, y_offset = 60):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                
                if row_index == 0:
                    alien_sprite = Alien("yellow", x, y)
                elif row_index == 1 or row_index == 2:
                    alien_sprite = Alien("green", x, y)
                else:
                    alien_sprite = Alien("red", x, y)
                self.aliens.add(alien_sprite)
        
        
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
            
    def collision_check(self):
        #Player shoots
        if self.player.sprite.shoots:
            for shoot in self.player.sprite.shoots:
                #Obstacle Collision
                if pygame.sprite.spritecollide(shoot, self.block, True):
                    shoot.kill()
                    
                #Alien Collision
                if pygame.sprite.spritecollide(shoot, self.aliens, True):
                    shoot.kill()
                    
                #Extra Collsion
                if pygame.sprite.spritecollide(shoot, self.extra, True):
                    shoot.kill()
                    
        #Alien shoot
        if self.alien_shoots:
            for shoot in self.alien_shoots:
                #Obstace Collision
                if pygame.sprite.spritecollide(shoot, self.block, True):
                    shoot.kill()
                    
                #Player Collsion
                if pygame.sprite.spritecollide(shoot, self.player, False):
                    shoot.kill()
                    print("a")
                    
        #Alien-player 
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.block, True)
                
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    exit()
                    
            
        
    
    def run_game(self):
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_postion_checker()
        self.extra_alien_time()
        
        self.alien_shoots.update()
        self.extra.update()
        
        self.player.sprite.shoots.draw(app.screen)
        self.player.draw(app.screen)
        self.block.draw(app.screen)
        self.aliens.draw(app.screen)
        self.alien_shoots.draw(app.screen)
        self.extra.draw(app.screen)
        
        self.collision_check()

class App:
    def __init__(self):
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game = Game(self)
        
        self.ALIENS_SHOOT_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ALIENS_SHOOT_EVENT,500)
        
        
        
    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.ALIENS_SHOOT_EVENT:
                    self.game.alien_shoot()
                    
            
                    
            self.screen.fill(BLACK)
            self.game.run_game()
                
            pygame.display.update()
            
        



if __name__ == "__main__":
    pygame.init()
    
    
    app = App()
    app.run()
