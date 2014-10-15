import cocos
import random
from game import resources
from cocos.director import director
from cocos.actions import *

class MoveCell(Move):
    def step(self, dt):
        super(MoveCell, self).step(dt)
        self.random()


    def random(self):
        """ random walk code"""
        if bool(random.getrandbits(1)):
            if bool(random.getrandbits(1)):
                self.target.set_position(self.target.position[0]+1, self.target.position[1])
            else:
                self.target.set_position(self.target.position[0]-1, self.target.position[1])
        else:
            if bool(random.getrandbits(1)):
                self.target.set_position(self.target.position[0], self.target.position[1]+1)
            else:
                self.target.set_position(self.target.position[0], self.target.position[1]-1)


class MoveToCell(Action):
    """
    Modified movement to target
    Done moving when past target
    """
    def init(self, dst_coords, *args, **kwargs):
        """Init method.

        :Parameters:
            `dst_coords` : (x,y)
                Coordinates where the sprite will be placed at the end of the action
        """
        self.end_position = dst_coords

    def start( self ):
        self.start_position = self.target.position
        self.delta = self.target.velocity
        self.end_X = self.X_diff()
        self.end_Y = self.Y_diff()


    def step(self,dt):
        print self.target.position
        self.target.set_position(self.target.position[0] + dt*self.delta[0], self.target.position[1] + dt*self.delta[1])
        self.random()

    def done(self):
        print self.end_position
        print self.target.position
        if ((not self.end_X == self.X_diff() ) and ( not self.end_Y == self.Y_diff() )):
            print self.end_X, " != ", self.X_diff()
            print self.end_Y, " != ", self.Y_diff()

        return ((not self.end_X == self.X_diff() ) and ( not self.end_Y == self.Y_diff() ))

    def X_diff(self):
        return (self.target.position[0] -  self.end_position[0] <= 0)

    def Y_diff(self):
        return (self.target.position[1] - self.end_position[1] <= 0)


    def random(self):
        """ random walk code"""
        if bool(random.getrandbits(1)):
            if bool(random.getrandbits(1)):
                self.target.set_position(self.target.position[0]+1, self.target.position[1])
            else:
                self.target.set_position(self.target.position[0]-1, self.target.position[1])
        else:
            if bool(random.getrandbits(1)):
                self.target.set_position(self.target.position[0], self.target.position[1]+1)
            else:
                self.target.set_position(self.target.position[0], self.target.position[1]-1)



class SpriteLayer( cocos.layer.Layer ):
    """"
    Layer to hold all and manage
    sprites in game window
    """

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

        x,y = director.get_window_size()
        print "Game Dimensions: ", x,"x", y

        # Initialize Position of Cell
        self.cell.x = 200
        self.cell.y = 200
        self.cell.velocity = (10, 0)
        # Add the cell to the layer
        self.add(self.cell)
        #self.cell.do(MoveBy((200, 0), 10))
        #self.cell.do(MoveCell())
        self.cell.do(MoveToCell((300,200)))

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


