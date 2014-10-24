import cocos
import random

"""
Rewriting my own movement classes because I don't like the Cocos Defaults
"""

class MoveTo(cocos.actions.base_actions.Action):
    """
    Given a set of coordinates, objects will move to these coordinates
    Future - make this dependent on object max_velocities in x and y

    Note:
    It is beyond me how the fuck self.target is set.
    I've searched all through the cocos source code and could not find it
    Perhaps target is something intrinsic to python objects?
    Or is it function `do`?
    """
    def init(self, coords, *args, **kwargs):
        """
        Generic as possible, this is inherited
        by all subclasses of MoveTo
        """
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
        """
        In one step, target moves 1 in x and y towards target
        In future, this step will be velocity-dependent
        """
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
        """
        MoveTo is done if our target ceases to exist,
            if we go out of bounds, or if we reach our target
        """
        if self.target == None:
            return True
        elif self.check_bounds(*self.end_position):
            return True
        else:
            return self.target.position == self.end_position


    def check_bounds(self, x = None, y = None):
        """
        Check boundaries of window
        Returns True if out of bounds
        """
        if x == None or y == None:
            if self.target.x < self.x_min:
                self.target.x = self.x_min
                self.target.direction = 0
                return True
            elif self.target.x > self.x_max:
                self.target.x = self.x_max
                self.target.direction = 1
                return True
            if self.target.y < self.y_min:
                self.target.y = self.y_min
                self.target.direction = 2
                return True
            elif self.target.y > self.y_max:
                self.target.y = self.y_max
                self.target.direction = 3
                return True
            return False
        else:
            if x < self.x_min or x > self.x_max:
                return True
            elif y < self.y_min or y > self.y_max:
                return True
            else:
                return False




    def checkbounds(self, x, y):
        """
        Check to verify x and y are not out of bounds
        This method is specifically for checking destination coordinates
        to verify that we are not going to pathfind to a destination out of bounds
        Return True if out of bounds
        """
        if self.x_max < x < self.x_min:
            return True
        elif self.y_max < y < self.y_min:
            return True
        else:
            return False



class MoveBy(MoveTo):
    """
    MoveTo subclass with relative coordinates rather than absolute
    """
    def init(self, coords):
        """
        Always inherit the super.init of MoveTo
        """
        super(MoveBy, self).init(coords)

    def start(self):
        """
        Translate our relative coordinates into absolute coordinates
        and then MoveTo superclass will handle the rest
        """
        x = self.target.position[0] + self.coords[0]
        y = self.target.position[1] + self.coords[1]
        self.end_position = x, y



class RandomWalk(cocos.actions.Move):
    """
    Random Walk motion, step +/- 0.5 in any direction per step
    """
    def step(self, dt):
        """
        Call random method every step
        """
        super(Move, self).step(dt)
        self.random()


    def random(self):
        """
        Random walk code - supposedly a very efficien way of doing this
        I chose 0.5, because steps of 1 looked too big
        """
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

