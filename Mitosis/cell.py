import pygame


#Class create Cell given position
class Cell(pygame.sprite.Sprite):
    def __init__(self, surface ,form, x, y):
        super().__init__()
        self.surface = surface
        self.form = form
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        
        self.image = self.create_form(form)
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def create_form(self, form):
        cell_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
        
        if form == "circle":
            pygame.draw.circle(cell_surface, self.color, (25, 25), 20)
            
        elif form == "ellipse": #y estara en el medio del circulo la elipse
            pygame.draw.ellipse(cell_surface, self.color, (0, 0, 40, 20))
        return cell_surface
        
        
        
    def update(self, direction):
        self.rect.x += direction
        self.rect.y += direction