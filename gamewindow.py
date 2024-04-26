import pyglet
from pyglet.math import Vec2
from settings import WIDTH,HEIGHT
from objects import Vehicle

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()

        self.vh1 = Vehicle(self.batch, WIDTH//2, HEIGHT//2)
        self.vh1.applyForce(Vec2(10,10))


    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def update(self, dt):
        self.vh1.update(dt)