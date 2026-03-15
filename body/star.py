import pygame # pyright: ignore[reportMissingImports]

class Star:
    def __init__(self, color, x_pos, y_pos, radius):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
    
    def draw(self, screen, camera):
        pos = camera.apply(self.x_pos, self.y_pos)
        radius = camera.apply_radius(self.radius)
        pygame.draw.circle(screen, self.color, pos, radius)