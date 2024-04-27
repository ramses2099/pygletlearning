
import pyglet
# loading assest images
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("ship_D.png")
bullet_image = pyglet.resource.image("laserRed01.png")
asteroid_image = pyglet.resource.image("meteor_small.png")

engien_image = pyglet.resource.image('effect_yellow.png')
engien_image.anchor_x = engien_image.width * 1.5
engien_image.anchor_y = engien_image.height / 2