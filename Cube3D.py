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

        self.add_intermediate_points()
        self.projected_points = [
             [n, n] for n in range(len(self.points))
        ]
    
    def add_intermediate_points(self):
        new_points = []
        for p in range(4):
            # Interpolar linealmente entre los dos puntos
            interpolated_points = np.linspace(self.points[p], self.points[(p+1) % 4], num=3, endpoint=False)
            new_points.extend(interpolated_points[1:])
            interpolated_points = np.linspace(self.points[p+4], self.points[((p+1) % 4) + 4], num=3, endpoint=False)
            new_points.extend(interpolated_points[1:])
            interpolated_points = np.linspace(self.points[p], self.points[(p+4)], num=3, endpoint=False)
            # Agregar los puntos intermedios a la lista
            new_points.extend(interpolated_points[1:])  # Omitir el primer punto para evitar duplicados

            
        
        self.points.extend(new_points)
        
        self.points.append([0.333, 0.3333, 1])
        self.points.append([-0.333, -0.3333, 1])
        self.points.append([0.333, -0.3333, 1])
        self.points.append([-0.333, 0.3333, 1])
        self.points.append([0.333, 0.3333, -1])
        self.points.append([-0.333, -0.3333, -1])
        self.points.append([0.333, -0.3333, -1])
        self.points.append([-0.333, 0.3333, -1])
#
        self.points.append([0.333,1, 0.3333])
        self.points.append([-0.333,1, -0.3333])
        self.points.append([0.333,1, -0.3333])
        self.points.append([-0.333,1, 0.3333])
        self.points.append([0.333,-1, 0.3333])
        self.points.append([-0.333,-1, -0.3333])
        self.points.append([0.333,-1, -0.3333])
        self.points.append([-0.333,-1, 0.3333])
#
        self.points.append([1,0.333, 0.3333])
        self.points.append([1,-0.333, -0.3333])
        self.points.append([1,0.333, -0.3333])
        self.points.append([1,-0.333, 0.3333])
        self.points.append([-1,0.333, 0.3333])
        self.points.append([-1,-0.333, -0.3333])
        self.points.append([-1,0.333, -0.3333])
        self.points.append([-1,-0.333, 0.3333])


        
        

            



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
        
    def connect_points(self, i, j, points, color):
        pygame.draw.line(app.screen, color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
        
    #def create_point(self, i , j , points):
       # pygame.draw.circle(app.screen, RED, ( (points[i][0] + points[j][0]),  points[j][1] ), 5)



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

            
            self.angle= 0.002
                
            self.cube.rotate(self.angle)
            
            i = 0
            for point in self.cube.points:
                x = int(point[0] * self.scale) + CENTER[0]
                y = int(point[1] * self.scale) + CENTER[1]
                
                self.cube.projected_points[i] = [x, y]
                pygame.draw.circle(self.screen, RED, (x, y), 5)
                i += 1
                
            for p in range(4):
                self.cube.connect_points(p, (p+1) % 4, self.cube.projected_points,"RED")
                #self.cube.create_point(p, (p+1) % 4, self.cube.projected_points)
                self.cube.connect_points(p+4, ((p+1) % 4) + 4, self.cube.projected_points,"YELLOW")
                self.cube.connect_points(p, (p+4),self.cube.projected_points,"ORANGE")
                

            pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()
