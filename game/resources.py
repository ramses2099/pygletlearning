
import pyglet
# loading assest images
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("ship_D.png")
bullet_image = pyglet.resource.image("laserRed01.png")
asteroid_image = pyglet.resource.image("meteor_small.png")