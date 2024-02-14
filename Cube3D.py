import pygame
import numpy as np
import math
from sys import exit


#Variables
WIDTH, HEIGHT = 1200, 800
FPS = 22
CENTER = (WIDTH//2, HEIGHT//2)
angle = 0

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
    [1, 0, 0],
    [0, 1, 0]
])

ROTATION_X = np.matrix([
    [1, 0,  0],
    [0, math.cos(angle), math.sin(angle) * -1],
    [0, math.sin(angle), math.cos(angle)]
    ])

ROTATION_Y = np.matrix([
    [math.cos(angle), 0,  math.sin(angle)],
    [0, 1, 0],
    [math.sin(angle) * -1, 0, math.cos(angle)]
    ])

ROTATION_Z = np.matrix([
    [math.cos(angle), math.sin(angle) * -1,  0],
    [math.sin(angle), math.cos(angle), 0],
    [0, 0,  1]
    ])



#Classes

class Cube:
    def __init__(self, app):
        self.points = POINTS
        self.color = "RED"
        self.screen = app.screen
        self.angle = 0
        self.rotation_x  = np.matrix([
                                    [math.cos(angle), 0,  math.sin(angle)],
                                    [0, 1, 0],
                                    [math.sin(angle) * -1, 0, math.cos(angle)]
                                    ])
        self.rotation_z = np.matrix([
                                    [math.cos(angle), math.sin(angle) * -1,  0],
                                    [math.sin(angle), math.cos(angle), 0],
                                    [0, 0,  1]
                                    ])
        
        self.rotation_matrix = np.eye(3)
        
    """def apply_rotation(self, axis, angle):
        if axis == 'x':
            rotation_matrix = np.matrix([
                [1, 0, 0],
                [0, math.cos(angle), -math.sin(angle)],
                [0, math.sin(angle), math.cos(angle)]
            ])
            
        elif axis == 'y':
            rotation_matrix = np.matrix([
                [math.cos(angle), 0, math.sin(angle)],
                [0, 1, 0],
                [-math.sin(angle), 0, math.cos(angle)]
            ])
            
        elif axis == 'z':
            rotation_matrix = np.matrix([
                [math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0],
                [0, 0, 1]
            ])
        else:
            rotation_matrix = np.eye(3)  

        self.rotation_matrix = np.dot(rotation_matrix, self.rotation_matrix)
        return self.rotation_matrix """
        
        
    def draw_points(self):
        self.angle += 0.01
        for point in self.points:
            rotated = np.dot(self.rotation_x, point.reshape(3,1))
            rotated = np.dot(self.rotation_x, rotated)
            
            
            proyected_point = np.dot(PROJECTION_MATRIX, rotated)
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
