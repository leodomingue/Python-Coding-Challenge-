import pygame
import pygame.gfxdraw
import random
import math

COLORS = ((238,199,119,255), (197,159,84,255),(204,175,99,255), (255,226,108,255), (189,157,56,255), (189,157,56,255))


#Class create Cell given position
class Cell(pygame.sprite.Sprite):
    def __init__(self, surface ,form, x, y):
        super().__init__()
        self.surface = surface
        self.form = form
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        
        #Give radius if self form is circle or a and b if is ellipse
        self.size = [random.randint(15,25) if self.form == "circle" else (random.randint(15,20),random.randint(15,20))]
        
        self.image = self.create_form(form)
        self.rect = self.image.get_rect(topleft = (x, y))
        
    #Create random points using polar coordenates
    def random_point_in_circle(self, radius, center):
        angle = random.uniform(0, 2 * math.pi)
        r = radius * math.sqrt(random.uniform(0, 1))
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        return (int(center[0] + x), int(center[1] + y))
    
    #Create random points using polar coordenates
    def random_point_in_ellipse(self, a, b, center):
        angle = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.uniform(0, 1))
        x = a * r * math.cos(angle)
        y = b * r * math.sin(angle)
        return (int(center[0] + x), int(center[1] + y))
        
    def create_form(self, form):
        if form == "circle":
            surface_WIDTH = (self.size[0]+10) * 2
            cell_surface = pygame.Surface((surface_WIDTH, surface_WIDTH), pygame.SRCALPHA)
        

            pygame.gfxdraw.filled_circle(cell_surface, surface_WIDTH//2, surface_WIDTH//2, self.size[0] + 8, (107,69,20,255)) #28
            pygame.gfxdraw.filled_circle(cell_surface, surface_WIDTH//2, surface_WIDTH//2, self.size[0] + 7, (229,190,117,255))
            pygame.gfxdraw.filled_circle(cell_surface, surface_WIDTH//2, surface_WIDTH//2, self.size[0] + 5, (255,224,153,255))
            pygame.gfxdraw.filled_circle(cell_surface, surface_WIDTH//2, surface_WIDTH//2, self.size[0] + 3, (139,102,35,255))
            pygame.gfxdraw.filled_circle(cell_surface, surface_WIDTH//2, surface_WIDTH//2, self.size[0], (240,190,122,255))
            
            #Create random pixels
            num_points = surface_WIDTH//2 * surface_WIDTH//2 
            for i in range(num_points):
                point = self.random_point_in_circle(self.size[0], (surface_WIDTH//2, surface_WIDTH//2)) 
                
                cell_surface.set_at(point, random.choice(COLORS))  
        
            
            
        elif form == "ellipse": 
            pygame.gfxdraw.filled_ellipse(cell_surface, 30, 30, 29, 19, (107,69,20,255))
            pygame.gfxdraw.filled_ellipse(cell_surface, 30, 30, 27, 17, (229,190,117,255))
            pygame.gfxdraw.filled_ellipse(cell_surface, 30, 30, 25, 15, (255,224,153,255))
            pygame.gfxdraw.filled_ellipse(cell_surface, 30, 30, 23, 13, (139,102,35,255))
            pygame.gfxdraw.filled_ellipse(cell_surface, 30, 30, 20, 10, (240,190,122,255))
            
            #Create random pixels
            num_points = 300  
            for i in range(num_points):
                point = self.random_point_in_ellipse(20, 10, (30, 30)) 
                
                cell_surface.set_at(point, random.choice(COLORS))  
            
            
        return cell_surface
        
        
        
    def update(self, direction):
        self.rect.x += direction
        self.rect.y += direction