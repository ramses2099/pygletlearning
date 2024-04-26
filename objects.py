from pyglet import shapes
from pyglet.math import Vec2
from settings import *

class Vehicle(object):
    def __init__(self, batch, x, y, radius=32):
      self.batch = batch
      self.radius = radius
      self.position = Vec2(x, y)
      self.velocity = Vec2(0 ,0)
      self.acceleration = Vec2(0, 0)
      self.shape = shapes.Circle(x=self.position.x, y=self.position.y, 
                                 radius=self.radius, color=GREEN,batch=self.batch)
      self.maxspeed = 0
      
    def applyForce(self, force: Vec2) ->None:
        self.acceleration.x = self.acceleration.x + force.x
        self.acceleration.y = self.acceleration.y + force.y
    
    def update(self, dt):        
        if(self.position.x > WIDTH - self.radius or self.position.x < self.radius):
            self.velocity.x *= -1 
        if(self.position.y > HEIGHT - self.radius or self.position.y < self.radius):
            self.velocity.y *= -1 

        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.shape.position = self.position
        # self.acceleration = Vec2(0,0)