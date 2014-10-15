import cocos
import random

class MoveCell(cocos.actions.Move):
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


class MoveToCell(cocos.actions.Action):
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
        self.target.set_position(self.target.position[0] + dt*self.delta[0], self.target.position[1] + dt*self.delta[1])
        self.random()

    def done(self):
        if ((not self.end_X == self.X_diff() ) and ( not self.end_Y == self.Y_diff() )):
            print "Destination Passed"

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

