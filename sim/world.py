import pygame # pyright: ignore[reportMissingImports]
from body.star import Star
from body.planet import Planet
from utils.orbit import Orbit
import json

class World:
    def __init__(self, screen, center_x, center_y):
        self.screen = screen
        with open("data/stars.json") as f:
            stars_data = json.load(f)
        with open("data/planets.json") as f:
            planets_data = json.load(f)
            
        sun = stars_data["sun"]
        self.star = Star(sun["color"], center_x, center_y, sun["radius"])
        
        earth = planets_data["earth"]
        self.earth = Planet(earth["color"], 
                            center_x - 300, 
                            center_y, 
                            earth["radius"], 
                            center_x, 
                            center_y,
                            300)
        
    def draw(self):
        self.star.draw(self.screen)
        self.earth.draw(self.screen)
    
    def update(self, dt):
        self.earth.update(dt)
        