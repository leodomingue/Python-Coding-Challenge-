import pygame
import numpy as np
from sys import exit


#Variables
WIDTH, HEIGHT = 1200, 800
FPS = 60
CENTER = (WIDTH//2, HEIGHT//2)

POINTS = []
POINTS.append(np.matrix([-1, -1, 1]))
POINTS.append(np.matrix([1, -1, 1]))
POINTS.append(np.matrix([1, 1, 1]))
POINTS.append(np.matrix([-1, 1, 1]))
POINTS.append(np.matrix([-1, -1, 1]))
POINTS.append(np.matrix([1, -1, 1]))
POINTS.append(np.matrix([1, 1, 1]))
POINTS.append(np.matrix([-1, 1, 1]))

PROJECTION_MATRIX = np.matrix([
    [1,0,0],
    [0,1,0]
])

#Classes

class Cube:
    def __init__(self, app):
        self.points = POINTS
        self.color = "RED"
        self.screen = app.screen
        
        
    def draw_points(self):
        for point in self.points:
            proyected_point = np.dot(PROJECTION_MATRIX, point.reshape(3,1))
            x_pos = int(proyected_point[0].item()) * 100  + CENTER[0]
            y_pos = int(proyected_point[1].item())  * 100 + CENTER[1]
            
            pygame.draw.circle(self.screen, self.color, (x_pos, y_pos), 5)
        
    


#Main Class
class App:
    def __init__(self):
        pygame.init()
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.cube = Cube(self)
        
    def run(self):
        while True:
            self.screen.fill("BLACK")
            self.cube.draw_points()
            
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
