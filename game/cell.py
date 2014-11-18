from game import physicalobject, resources, movement, util, actions, food
import random


class Cell(physicalobject.PhysicalObject):
    """
    Cells! The main objects in the game
    """

    def __init__(self, energy = 50, *args, **kwargs):
        """
        Constructor for Cell
        """
        super(Cell, self).__init__(resources.cell_image, *args, **kwargs)
        self.hungry = True
        self.target = None
        self.last_target = None
        self.action = None
        # string version of Type
        self.Type = 'cell'

        # Cell Stats
        self.energy = energy
        self.energy_max = 100
        self.age = 1



    def update(self, dt):
        """
        Update Cell
        """
        self.alive()
        super(Cell, self).update(dt)
        self.timers()
        if self.action == None:
            self.behavior()
        elif self.action.done() == True:
            self.behavior()


    def alive(self):
        """
        Check to see if cell is still alive
        """
        if self.energy <= 0:
            self.dead = True


    def timers(self):
        """
        All timer intervals listed here
        """
        if self.time % 100 == 0:
            self.age += 1
            self.energy += -1
        if self.time % 120 == 0:
            if self.reproductive():
                self.reproduce()


    def reproductive(self):
        print "stats"
        print "energy", self.energy
        print "age", self.age
        if self.energy > 80 and self.age > 20:
            return True
        else:
            return False

    def reproduce(self):
        """
        Create a new cell and lose some energy
        """
        newcell = Cell(position=(self.x, self.y), color=self.color, energy = 30)
        self.new_obj.append(newcell)
        self.energy += -40




    def behavior(self):
        """
        Decision Tree for determining action for this time step
        """
        if self.hungry:
            self.acquirefood()
        else:
            self.wander()


    def acquirefood(self):
        """
        Process of acquiring food
        """
        if not self.target == None and self.target.dead == False:
            self.pathfind()
            self.last_target = self.target
            self.target = None
        elif not self.last_target == None:
            self.eat()
            self.last_target = None
        else:
            self.wander()
            self.search()


    def pathfind(self):
        """
        Move in direction of target
        """
        self.action = self.do(movement.MoveTo(self.target.position))


    def wander(self):
        """
        Wander aimlessly
        """
        self.action = self.do(movement.MoveBy((random.randint(-30, 30), (random.randint(-30, 30)))))


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


    def eat(self):
        """
        Set action to eating
        """
        self.action = actions.Eat(self.last_target)


    def handle_collision_with(self, other_object):
        """
        Collision handler for cells
        """
        if other_object.Type == 'food':
            self.energy += 1

    def delete(self):
        """
        Handle Cell Death
        """
        super(Cell, self).delete()
        newfood = food.Food(position=(self.x, self.y))
        self.new_obj.append(newfood)
