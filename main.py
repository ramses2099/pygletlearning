import pyglet
from settings import WIDTH, HEIGHT, CAPTION, FPS
from gamewindow import GameWindow

if __name__ == "__main__":
    window = GameWindow(width=WIDTH, height=HEIGHT, caption=CAPTION, resizable=False)
    pyglet.clock.schedule_interval(window.update, FPS)
    pyglet.app.run() 