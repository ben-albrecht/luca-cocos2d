import cocos
import random

"""
Rewriting my own movement classes because I don't like the Cocos Defaults
"""

class MoveTo(cocos.actions.base_actions.Action):
    def init(self, coords, *args, **kwargs):
        super(MoveTo, self).init(*args, **kwargs)
        self.coords = coords
        self.x_max, self.y_max = cocos.director.director.get_window_size()
        self.x_min, self.y_min = 0, 0


    def start(self):
        """
        Never inherit start
        """
        self.end_position = self.coords


    def step(self, dt):
        x = self.target.position[0]
        y = self.target.position[1]
        if self.end_position[0] > x:
            dx = 1
        elif self.end_position[0] < x:
            dx = -1
        else:
            dx = 0

        if self.end_position[1] > y:
            dy = 1
        elif self.end_position[1] < y:
            dy = -1
        else:
            dy = 0

        self.target.set_position(x + dx, y + dy)
        self.check_bounds()


    def done(self):
        if self.target == None:
            return True
        else:
            return self.target.position == self.end_position


    def check_bounds(self):
        """
        Check boundaries of window
        """
        if self.target.x < self.x_min:
            self.target.x = self.x_min
            self.target.direction = 0
        elif self.target.x > self.x_max:
            self.target.x = self.x_max
            self.target.direction = 1
        if self.target.y < self.y_min:
            self.target.y = self.y_min
            self.target.direction = 2
        elif self.target.y > self.y_max:
            self.target.y = self.y_max
            self.target.direction = 3


class MoveBy(MoveTo):
    def init(self, coords):
        super(MoveBy, self).init(coords)

    def start(self):
        x = self.target.position[0] + self.coords[0]
        y = self.target.position[1] + self.coords[1]
        self.end_position = x, y



class RandomWalk(cocos.actions.Move):
    def step(self, dt):
        super(Move, self).step(dt)
        self.random()


    def random(self):
        """ random walk code"""
        if bool(random.getrandbits(1)):
            if bool(random.getrandbits(1)):
                self.target.set_position(self.target.position[0]+.05, self.target.position[1])
            else:
                self.target.set_position(self.target.position[0]-.05, self.target.position[1])
        else:
            if bool(random.getrandbits(1)):
                self.target.set_position(self.target.position[0], self.target.position[1]+.05)
            else:
                self.target.set_position(self.target.position[0], self.target.position[1]-.05)

