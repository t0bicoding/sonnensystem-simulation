import pygame # pyright: ignore[reportMissingImports]
import json

class Planet:
    def __init__(self, color, x_pos, y_pos, radius, center_x, 
                 center_y, orbit_radius):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        
        self.center_x = center_x
        self.center_y = center_y
        self.border_thickness = 1
        self.border_color = "grey"
        self.orbit_radius = orbit_radius
        self.orbit_speed = 1
        

    def draw(self, screen):
        # Planet Orbit
        pygame.draw.circle(screen, 
                           self.border_color, 
                           (self.center_x, self.center_y), 
                           self.orbit_radius, 
                           self.border_thickness)
        # Planet
        pygame.draw.circle(screen, 
                           self.color, 
                           (self.x_pos, self.y_pos), 
                           self.radius)
        
    def update(self, dt):
        dt = dt