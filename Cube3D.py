import pygame
import numpy
from sys import exit


#Variables
WIDTH, HEIGHT = 1200, 800
FPS = 60

#Classes


#Main Class
class App:
    def __init__(self):
        pygame.init()
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            self.screen.fill("BLACK")
            
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
