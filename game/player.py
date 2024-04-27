import math
import pyglet
from pyglet.window import key
from resources import player_image, engien_image
from physicalobject import PhysicalObject


class Player(PhysicalObject):
    def __init__(self, *args, **kwargs):
      super().__init__(img=player_image, *args, **kwargs)
      
      self.thrust = 300.0
      self.rotate_speed = 200.0
      
      self.engine_sprite = pyglet.sprite.Sprite(img=engien_image, *args, **kwargs)
      self.engine_sprite.visible = False
      
      self.key_handler = key.KeyStateHandler()
                 
    def update(self, dt):
        super(Player, self).update(dt)
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
            
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            # engine
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x - self.width / 2
            self.engine_sprite.y = self.y - self.height
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False