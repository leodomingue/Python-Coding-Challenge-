import pygame
import random
import math
from sys import exit


#Variables
WIDTH, HEIGHT = 1200, 800
FPS = 60
STAR_QUANT = 100
CENTER = (WIDTH//2, HEIGHT//2)
COLORS = ["red", "yellow", "blue", "green", "orange", "purple"]
VECTOR_3 = pygame.math.Vector3
VECTOR_2 = pygame.math.Vector2

#Classes

#class star
class Star:
    def __init__(self, app):
        self.distance_z = 40
        self.screen = app.screen
        self.pos3d = self.get_pos()
        self.color = random.choice(COLORS)
        self.vel = random.uniform(0.10, 0.50)
        self.size = random.randint(3,10)
        
    
    def get_pos(self):
        #POLARS COORDINATES
        angle = random.uniform(0, 2 * math.pi)
        radius = random.randint(0, HEIGHT)
        pos_x = radius * math.sin(angle)
        pos_y = radius * math.cos(angle)
        return VECTOR_3(pos_x, pos_y, self.distance_z)
    
    def update_move(self):
        pass
    
    def draw_star(self):
        pass
    
#SET OF STARS
class StarField:
    def __init__(self, app):
        self.stars = []
        for i in range(STAR_QUANT):
            star = Star(app)
            self.stars.append(star)
        
    def run(self):
        for star in self.stars:
            star.update_move()
            star.draw_star()
        


#Main Class
class App:
    def __init__(self):
        pygame.init()
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.starfield = StarField(self)
        
    def run(self):
        while True:
            self.screen.fill("black")
            self.starfield.run()
            
            #Update all the screen
            pygame.display.flip()
            for event in pygame.event.get():
                
                #Activates when touch quit 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.clock.tick(FPS)

#Start App
if __name__ == "__main__":
    app = App()
    app.run()
