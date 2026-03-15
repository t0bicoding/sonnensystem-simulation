import pygame # pyright: ignore[reportMissingImports]
import math
import json

class Planet:
    def __init__(self, center_x, center_y, name):
        
        with open("data/planets.json") as f:
            data = json.load(f)
        planet = data[name]
        
        with open("data/orbits.json") as f:
            data = json.load(f)    
        orbits = data["planets"]

        self.x_pos = center_x - planet["distance"]
        self.y_pos = center_y
        self.color = planet["color"]
        self.radius = planet["radius"] 
        self.orbit_speed = planet["orbit_speed"] / 10
        
        self.center_x = center_x
        self.center_y = center_y
        self.border_thickness = orbits["thickness"]
        self.border_color = orbits["color"]
        self.orbit_radius = planet["distance"]
        self.angle = 0.0
        

    def draw(self, screen, camera):
        # Planet Orbit
        center = camera.apply(self.center_x, self.center_y)
        orbit_radius = camera.apply_radius(self.orbit_radius)
        pygame.draw.circle(screen,
                           self.border_color,
                           center,
                           orbit_radius,
                           self.border_thickness)
        # Planet
        pos = camera.apply(self.x_pos, self.y_pos)
        radius = camera.apply_radius(self.radius)
        pygame.draw.circle(screen,
                           self.color,
                           pos,
                           radius)
        
    def update(self, dt):
        self.angle += self.orbit_speed * dt
        self.x_pos = self.center_x + math.cos(self.angle) * self.orbit_radius
        self.y_pos = self.center_y + math.sin(self.angle) * self.orbit_radius