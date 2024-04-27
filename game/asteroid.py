import pyglet
from resources import *
from load import *
from player import Player

WIDTH = 800
HEIGHT = 600
CAPTION = "Game Asteroid"
FPS =  1/120.0

game_window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption=CAPTION)
main_batch = pyglet.graphics.Batch()

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    
center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=580, batch=main_batch)
level_label = pyglet.text.Label(text="My Amazing Game", x=game_window.width//2,
                                y=game_window.height//2,
                                anchor_x='center', batch=main_batch)

player_ship = Player(x=400, y=300, batch=main_batch)
asteroids = asteroids(3, player_ship.position, main_batch)

player_lives = player_lives(3, main_batch)

game_objects = [player_ship] + asteroids
game_window.push_handlers(player_ship.key_handler)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):    
    for obj in game_objects:
        obj.update(dt)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, FPS)
    pyglet.app.run()