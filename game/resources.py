import pyglet
from game import util

# Set resource path and reindex
pyglet.resource.path = ["./resources"]
pyglet.resource.reindex()

# Load the cell image and center it
cell_image = pyglet.resource.image("cell.png")
util.center_image(cell_image)
