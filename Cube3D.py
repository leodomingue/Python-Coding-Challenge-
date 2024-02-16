import pygame
import numpy as np
from math import *

#Variables
FPS = 60
WIDTH, HEIGHT = 1200, 800
CENTER = (WIDTH//2, HEIGHT//2)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Cube:
    def __init__(self, app):
        self.app = app
        self.points = [
            np.array([-1, -1, 1]),
            np.array([1, -1, 1]),
            np.array([1,  1, 1]),
            np.array([-1, 1, 1]),
            np.array([-1, -1, -1]),
            np.array([1, -1, -1]),
            np.array([1, 1, -1]),
            np.array([-1, 1, -1])
        ]
        self.projected_points = [
             [n, n] for n in range(len(self.points))
        ]
        

    def rotate(self, angle):
        rotation_z = np.array([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1],
        ])
        
        rotation_x = np.array([
                [1, 0, 0],
                [0, cos(angle), -sin(angle)],
                [0, sin(angle), cos(angle)],
        ])
        
        self.points = [np.dot(rotation_z, point) for point in self.points]

        self.points = [np.dot(rotation_x, point) for point in self.points]
        
    def connect_points(self, i, j, points):
        pygame.draw.line(app.screen, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


class App:
    def __init__(self):
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.scale = 100
        self.angle = 0
        self.cube = Cube(App)
        
    

    def run(self):
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(BLACK)

            
            self.angle= 0.02
                
            self.cube.rotate(self.angle)
            
            i = 0
            for point in self.cube.points:
                x = int(point[0] * self.scale) + CENTER[0]
                y = int(point[1] * self.scale) + CENTER[1]
                
                self.cube.projected_points[i] = [x, y]
                pygame.draw.circle(self.screen, RED, (x, y), 5)
                i += 1
                
            for p in range(4):
                self.cube.connect_points(p, (p+1) % 4, self.cube.projected_points)
                self.cube.connect_points(p+4, ((p+1) % 4) + 4, self.cube.projected_points)
                self.cube.connect_points(p, (p+4), self.cube.projected_points)

            pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()
