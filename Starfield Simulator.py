import pygame
import random
import math
from sys import exit


#Variables
WIDTH, HEIGHT = 1200, 800
FPS = 60
STAR_QUANT = 100
CENTER = (WIDTH//2, HEIGHT//2)
COLORS = ["#FF0000", "#FFFF00", "#0000FF", "#00FF00", "#FFA500", "#800080"]

DISTANCE_Z = 30
VECTOR_3 = pygame.math.Vector3
VECTOR_2 = pygame.math.Vector2

CENTER_RADIUS = 10
TRAIL_LENGTH = 5

#Classes

#class star
class Star:
    def __init__(self, app):
        self.distance_z = 40
        self.screen = app.screen
        self.pos3d = self.get_pos()
        self.color = random.choice(COLORS)
        self.vel = random.uniform(0.20, 0.55)
        self.size = 10
        self.star_pos = VECTOR_2(0,0)
        self.trail = []
        
    
    def get_pos(self):
        #POLAR COORDINATE
        angle = random.uniform(0, 2 * math.pi)
        radius = random.randint(700, HEIGHT)
        pos_x = radius * math.sin(angle)
        pos_y = radius * math.cos(angle)
        return VECTOR_3(pos_x, pos_y, DISTANCE_Z)
    
    def update_move(self):
        self.pos3d.z -= self.vel
        if self.pos3d.z < 0.1:
            self.pos3d = self.get_pos()
            self.size = random.randint(4,10)
            
        # Store prev location
        if self.star_pos != VECTOR_2(0,0):
            self.trail.append(self.star_pos.copy())
            if len(self.trail) > TRAIL_LENGTH:
                self.trail.pop(0)
            
        self.star_pos = VECTOR_2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        
    
    def draw_star(self):
        pygame.draw.rect(self.screen, self.color, (*self.star_pos, self.size, self.size))
        for i in range(len(self.trail)-1):
            if 0 < self.trail[i][0] <= 1200 and 0 < self.trail[i][1] <=800:
                pygame.draw.line(self.screen, self.color, self.trail[i], self.trail[i+1],width=self.size-2)
    
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
