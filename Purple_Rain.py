import pygame
import random

#VARIABLE
WIDTH = 800
HEIGHT = 800

#COLORS
RAIN_COLOR = (138, 43, 226)
BAKCGROUND_COLOR =(239, 230, 250)

#Class to represent a raindrop
class Raindrop:
    
    #Each raindrop contatin an x and an y coordenates and different speed
    def __init__(self,app):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-1000000, WIDTH)
        self.speed = random.randint(1,2)
        self.length = random.randint(10,13)
    
    #Fall Logic
    def fall(self):
        self.y += self.speed
        self.speed += 0.004
        if self.y > HEIGHT:
            self.x = random.randint(0, WIDTH)
            self.y = 0
            self.speed = random.uniform(1,2)
    
    #Draw a raindrop
    def draw_raindrop(self):
        pygame.draw.line(app.screen, RAIN_COLOR, (self.x, self.y), (self.x, self.y + self.length), int(self.length-9))

#Main Window
class App:
    def __init__(self):
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.raindrops = [Raindrop(self) for _ in range(50)]
        
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
                    
            self.screen.fill(BAKCGROUND_COLOR)
            for raindrop in self.raindrops:
                raindrop.fall()
                raindrop.draw_raindrop()
                
            pygame.display.flip()
            
        



if __name__ == "__main__":
    app = App()
    app.run()
