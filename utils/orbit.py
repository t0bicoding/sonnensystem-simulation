import pygame # pyright: ignore[reportMissingImports]

class Orbit:
    def __init__(self, color, x_pos, y_pos, radius, border_thickness):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.border_thickness = border_thickness
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius, self.border_thickness)