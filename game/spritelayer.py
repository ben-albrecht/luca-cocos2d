import cocos
import random
from game import resources

class SpriteLayer( cocos.layer.Layer ):
    """" Layer to hold all sprites in game window """

    # Enable pyglet's events for this class
    is_event_handler = True

    def __init__( self, index=1 ):
        """
        Initialize some sprites on the screen and call the
        schedule function
        """

        # Superclass constructor
        super(SpriteLayer, self ).__init__()
        # Set index - don't know this purpose yet
        self.index = index

        # Read in the cell image and center it
        # This stuff should be done in resources
        self.image = resources.cell_image
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.cell = cocos.sprite.Sprite(self.image)

        # Add the cell to the layer
        self.add(self.cell)

        # Initialize Position of Cell
        self.cell.x = 400
        self.cell.y = 300
        # Alternatively: Both at once
        #self.cell.position = 400,300

        # Call update function every frame
        self.schedule(self.update)

        # Alternatively: Call update function every 1 second
        # - This is really shitty intervals, just an example
        #self.schedule_interval(self.update, 1)



    def update(self, dt):
        self.move()


    def move(self):
        self.random()


    def random(self):
        """ random walk code"""
        if bool(random.getrandbits(1)):
            if bool(random.getrandbits(1)):
                self.cell.x += 1
            else:
                self.cell.x += -1
        else:
            if bool(random.getrandbits(1)):
                self.cell.y += 1
            else:
                self.cell.y += -1
