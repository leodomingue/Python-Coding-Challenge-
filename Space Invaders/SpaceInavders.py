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
        
        #HEALTH AND SCORE
        self.health_player = 3
        self.live_surf = pygame.image.load("Space Invaders/assets/player.png").convert_alpha()
        self.font = pygame.font.Font("Space Invaders/assets/space_invaders.ttf", 30)
        
        self.score = 0
        
        
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
        self.rows = 4
        self.columns = 4
        self.alien_setup(rows=self.rows, cols=self.columns)
        self.alien_direction = 1
        self.alien_shoots = pygame.sprite.Group()
        
        #Alien Extra
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = random.randint(400, 800)
        
        #Music and sound
        self.music = pygame.mixer.Sound("Space Invaders/assets/music.mp3")
        self.music.set_volume(0.1)
        self.music.play(loops = -1)
        
        self.speed = 1
        
        self.level = 0
        
        #Background
        self.planet_1 = pygame.image.load("Space Invaders/assets/Planets/earth.png").convert_alpha()
        self.planet_2 = pygame.image.load("Space Invaders/assets/Planets/mars.png").convert_alpha()
        self.planet_3 = pygame.image.load("Space Invaders/assets/Planets/planet.png").convert_alpha()
        self.planet_4 = pygame.image.load("Space Invaders/assets/Planets/purple planet.png").convert_alpha()
        
        self.planet = self.planet_1
        
    def display_planet(self, planet):
        image_rect = planet.get_rect()
        x =(WIDTH - image_rect.width)//2
        y =(HEIGHT - image_rect.height)//2
        app.screen.blit(planet, (x, y))
        
    def display_score(self):
        score_text = "Puntuacion: "+str(self.score)
        text = self.font.render(score_text, False, "White")
        text_rect = text.get_rect(topleft=(0,0))
        app.screen.blit(text, text_rect)
        
    def display_lives(self):
        lives_text = "vidas: " + str(self.health_player)
        text = self.font.render(lives_text, False, "white")
        text_rect = text.get_rect(topright=(WIDTH - self.live_surf.get_size()[0]-20, 0))
        app.screen.blit(text, text_rect)
        
        app.screen.blit(self.live_surf, (WIDTH - self.live_surf.get_size()[0],0))
        app.screen.blit
        
    def extra_alien_time(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(random.choice(["right","left"]), WIDTH))
            self.extra_spawn_time = random.randint(400, 800)
        
    def alien_postion_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= WIDTH:
                self.alien_direction = -self.speed
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction =  self.speed
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
        
        
    def create_obstacle(self, color, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, color, x, y)
                    self.block.add(block)
                    
    def create_multiple_obstacle(self, x_start, y_start, *offset):
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "gray", "cyan", "magenta", "lime", "teal", "olive", "navy", "maroon", "aquamarine", "coral"])
        for offset_x in offset:
            self.create_obstacle(color, x_start, y_start, offset_x)
            
    def collision_check(self):
        #Player shoots
        if self.player.sprite.shoots:
            for shoot in self.player.sprite.shoots:
                #Obstacle Collision
                if pygame.sprite.spritecollide(shoot, self.block, True):
                    shoot.kill()
                    
                #Alien Collision
                alien_hit = pygame.sprite.spritecollide(shoot, self.aliens, True)
                if alien_hit:
                    for alien in alien_hit:
                        self.score += alien.value
                    shoot.kill()

                    
                #Extra Collsion
                if pygame.sprite.spritecollide(shoot, self.extra, True):
                    shoot.kill()
                    self.score += 1000
                    self.health_player += 1
                    
        #Alien shoot
        if self.alien_shoots:
            for shoot in self.alien_shoots:
                #Obstace Collision
                if pygame.sprite.spritecollide(shoot, self.block, True):
                    shoot.kill()
                    
                #Player Collsion
                if pygame.sprite.spritecollide(shoot, self.player, False):
                    shoot.kill()
                    self.health_player -= 1
                    
        #Alien-player 
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.block, True)
                
                if pygame.sprite.spritecollide(alien, self.player, False):
                    self.lose_screen()
                    
            
    def win_screen(self):
        if not self.aliens.sprites():
            self.app.screen.fill("BLACK")
            self.aliens.empty()
            self.alien_shoots.empty()
            self.extra.empty()
            self.block.empty()
            
            pause = True
            while pause:
                #Text
                
                win_text = f"Has ganado el nivel {self.level}"
                text = self.font.render(win_text, False, "White")
                text_rect = text.get_rect(center = (WIDTH/2, HEIGHT/2))
                app.screen.blit(text, text_rect)
                
                next_level_text = "Pulsa J para ir al siguiente nivel"
                next_text = self.font.render(next_level_text, False, "White")
                next_level__rect = next_text.get_rect(center = (WIDTH/2, HEIGHT/2 + 50))
                app.screen.blit(next_text, next_level__rect)
                
                
                #Variables
                self.player.draw(app.screen)
                self.display_lives()
                self.display_score()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
                
                #Options
                keys = pygame.key.get_pressed()
                if keys[pygame.K_j]:
                    #New Setup
                    self.aliens = pygame.sprite.Group()
                    self.level += 1
                    
                    if self.level % 2 == 1:
                        self.rows += 1
                        self.columns += 1
                    else:
                        self.speed = self.speed + 1
                        
                    if self.level >= 8:
                        self.planet = self.planet_4
                    elif self.level >= 6:
                        self.planet = self.planet_3
                    elif self.level >= 3:
                        self.planet = self.planet_2
                    self.alien_setup(rows=self.rows, cols=self.columns)
                    self.alien_direction = 2
                    self.alien_shoots = pygame.sprite.Group()
                    self.alien_postion_checker()
                    self.create_multiple_obstacle(WIDTH/20, 650, *self.obstacle_x_positions)
                    
                    pause = False
                pygame.display.update()
                
    def lose_screen(self):
        self.app.screen.fill("BLACK")
        self.display_planet(self.planet)
        self.aliens.empty()
        self.alien_shoots.empty()
        self.extra.empty()
        self.block.empty()
            
        pause = True
        while pause:
                #Text
                
            win_text = "Has perdido"
            text = self.font.render(win_text, False, "White")
            text_rect = text.get_rect(center = (WIDTH/2, HEIGHT/2))
            app.screen.blit(text, text_rect)
                
            next_level_text = "Pulsa J para reinicar"
            next_text = self.font.render(next_level_text, False, "White")
            next_level__rect = next_text.get_rect(center = (WIDTH/2, HEIGHT/2 + 50))
            app.screen.blit(next_text, next_level__rect)
                
                
            #Variables
            self.player.draw(app.screen)
            self.display_lives()
            self.display_score()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                
                #Options
            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                    #New Setup
                self.aliens = pygame.sprite.Group()
                self.columns = 4
                self.rows =4
                self.alien_setup(rows=self.rows, cols=self.columns)
                self.alien_direction = 1
                self.alien_shoots = pygame.sprite.Group()
                self.alien_postion_checker()
                self.speed = 1
                self.create_multiple_obstacle(WIDTH/20, 650, *self.obstacle_x_positions)
                self.score = 0
                self.health_player = 3
                self.level = 0
                
                self.planet = self.planet_1
                self.display_planet(self.planet)
                    
                    
                pause = False
            pygame.display.update()
        
        
    
    def run_game(self):
        self.display_planet(self.planet)
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
        self.display_lives()
        self.display_score()
        
        if not self.aliens:
            self.win_screen()
            
        if self.health_player == -1:
            self.lose_screen()

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
