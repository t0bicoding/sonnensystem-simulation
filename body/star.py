import pygame # pyright: ignore[reportMissingImports]

class Star:
    def __init__(self, color, x_pos, y_pos, radius):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)