from body.star import Star
from body.planet import Planet
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
        
        mercury = planets_data["mercury"]
        self.mercury = Planet(mercury["color"], 
                            center_x - 200, 
                            center_y, 
                            mercury["radius"], 
                            center_x, 
                            center_y,
                            200,
                            1.5)
        
        venus = planets_data["venus"]
        self.venus = Planet(venus["color"], 
                            center_x - 300, 
                            center_y, 
                            venus["radius"], 
                            center_x, 
                            center_y,
                            300,
                            1.3)
        
        earth = planets_data["earth"]
        self.earth = Planet(earth["color"], 
                            center_x - 400, 
                            center_y, 
                            earth["radius"], 
                            center_x, 
                            center_y,
                            400,
                            1)
        
    def draw(self):
        self.star.draw(self.screen)
        self.mercury.draw(self.screen)
        self.venus.draw(self.screen)
        self.earth.draw(self.screen)
        
    
    def update(self, dt):
        self.earth.update(dt)
        self.mercury.update(dt)
        self.venus.update(dt)
        