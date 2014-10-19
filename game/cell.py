import cocos
from game import physicalobject, resources, movement, util, actions
import random


class Cell(physicalobject.PhysicalObject):
    """
    Cells! The main objects in the game
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for Cell
        """
        super(Cell, self).__init__(resources.cell_image, *args, **kwargs)
        self.hungry = True
        self.target = None
        self.last_target = None
        self.action = None
        # Whether or not we are eating
        self.Type = 'cell'
        self.energy = 50
        self.energy_max = 100



    def update(self, dt):
        """
        Update Cell
        """
        super(Cell, self).update(dt)
        if self.action == None:
            self.behavior()
        elif self.action.done() == True:
            self.behavior()





    def behavior(self):
        """
        Decision Tree for determining action for this time step
        """
        if self.hungry:
            self.acquirefood()
        else:
            self.wander()


    def acquirefood(self):
        if not self.target == None and self.target.dead == False:
            self.pathfind()
        elif not self.last_target == None:
            if self.nearfood():
                self.eat()
        else:
            self.wander()
            self.search()


    def pathfind(self):
        """
        Move in direction of target
        """
        self.action = self.do(movement.MoveTo(self.target.position))
        #self.action = self.do(actions.Eat(self.target))
        self.last_target = self.target
        self.target = None


    def wander(self):
        """
        Wander aimlessly
        """
        self.action = self.do(movement.MoveBy((random.randint(-50, 50), (random.randint(-50, 50)))))


    def search(self):
        """
        Search field of view for food target
        """
        self.inview = [self]
        self.target = None

        self.search_radius = 100
        for obj in (i[1] for i in self.objects):
            if abs(obj.x - self.x) < self.search_radius:
                if abs(obj.y - self.y) < self.search_radius:
                        if util.distance((obj.x, obj.y), (self.x, self.y)) < self.search_radius**2:
                            self.inview.append(obj)
                            if obj.Type == 'food':
                                self.target = obj
                                print "target found:"
                                print obj.Type, obj.position

    def nearfood(self):
        """
        Last check to make sure we don't start eating without
        food colliding with cell
        """
        other_object = self.last_target
        collision_distance = (self.image.width * 0.5 * self.scale + \
                         other_object.scale * other_object.image.width * 0.5)
        collision_distance_squared = collision_distance ** 2
        actual_distance_squared = util.distance(self.position, other_object.position)
        return (actual_distance_squared <= collision_distance_squared)


    def eat(self):
        self.action = actions.Eat(self.last_target)
        self.last_target = None


    def handle_collision_with(self, other_object):
        if other_object.Type == 'food':
            self.energy += 1
