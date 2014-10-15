import cocos
import random
from game import resources, movement, colors
from cocos.director import director
from cocos.actions import *


class SpriteLayer( cocos.layer.ColorLayer ):
    """"
    Layer to hold all and manage
    sprites in game window
    """

    # Enable pyglet's events for this class
    is_event_handler = True

    def __init__( self, *args, **kwargs ):
        """
        Initialize some sprites on the screen and call the
        schedule function
        """

        # Superclass constructor
        super(SpriteLayer, self ).__init__(*args, **kwargs)

        # Read in the cell image and center it
        # This stuff should be done in resources
        self.image = resources.cell_image
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.cell = cocos.sprite.Sprite(self.image, position=(200,200), color=colors.blue)
        self.cell2 = cocos.sprite.Sprite(self.image, position=(100,100), color=colors.cyan)

        x,y = director.get_window_size()
        print "Game Dimensions: ", x,"x", y

        # Initialize Position of Cell
        self.cell.velocity = (10, 0)
        self.cell2.velocity = (50, 50)
        # Add the cell to the layer
        self.add(self.cell)
        self.add(self.cell2)
        #self.cell.do(MoveBy((200, 0), 10))
        #self.cell.do(MoveCell())
        self.cell.do(movement.MoveToCell((300,200)))
        self.cell2.do(movement.MoveToCell((300,200)))

        # Alternatively: Both at once
        #self.cell.position = 400,300

        # Call update function every frame
        #self.schedule(self.update)

        # Alternatively: Call update function every 1 second
        # - This is really shitty intervals, just an example
        #self.schedule_interval(self.update, 1)



    def update(self, dt):
        self.move()


    def move(self):
        self.random()


