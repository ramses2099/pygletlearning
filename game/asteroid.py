import pyglet
from resources import *

WIDTH = 800
HEIGHT = 600
CAPTION = "Game Asteroid"

game_window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption=CAPTION)

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    
center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=580)
level_label = pyglet.text.Label(text="My Amazing Game", x=game_window.width//2,
                                y=game_window.height//2,
                                anchor_x='center')

player_ship = pyglet.sprite.Sprite(img=player_image, x=400, y=300)

@game_window.event
def on_draw():
    game_window.clear()
    
    level_label.draw()
    score_label.draw()
    player_ship.draw()

if __name__ == "__main__":
    pyglet.app.run()