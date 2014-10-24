import cocos
import random
from game import resources, colors, physicalobject, cell, food
from cocos.director import director
from cocos.actions import *


class SpriteLayer( cocos.layer.Layer ):
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
        # Internal Clock of SpriteLayer
        self.time = 0

        # Superclass constructor
        super(SpriteLayer, self ).__init__(*args, **kwargs)

        # Get coordinates of upper right corner (max size)
        self.x_max, self.y_max = director.get_window_size()
        print "Game Dimensions: ", self.x_max,"x", self.y_max

        # Load objects into the game - spawns cells, food, etc.
        self.load()

        # Set up scheduler to call update function every frame
        self.schedule(self.update)


    def load(self):
        """
        Initial load method for start of game
        Eventually this will call a general spawn function
        self.spawn(10, Type = 'cell')
        """
        self.add(cell.Cell(position=(300,300), color=colors.blue))
        self.add(cell.Cell(position=(300,300), color=colors.blue))
        self.add(cell.Cell(position=(300,300), color=colors.blue))
        #self.children[0][1].get_objlist(self.children)

        #self.add(cell.Cell(position=(300,200), color=colors.blue))
        self.add(food.Food(position=(random.randint(250,350), random.randint(250,350))))
        self.add(food.Food(position=(random.randint(250,350), random.randint(250,350))))
        #self.add(food.Food(position=(random.randint(0, x), random.randint(0,y))))
        """
        Example of self.spawn:
        while self.counter[self.indices[Type]] < Num:
            new_obj = self.types[Type](box=self.box,
                                name=Type+str(self.counter[self.indices[Type]]),
                                x=random.randint(self.xmin, self.xmax),
                                y=random.randint(self.ymin, self.ymax),
                                batch=self.Batch)

            collides = False
            for i in xrange(len(self.objects)):
                other_obj = self.objects[i]
                if new_obj.collides_with(other_obj):
                    collides = True
                    break
            if not collides:
                self.objects.append(new_obj)
                self.counter[self.indices[Type]] += 1
        """


    def update(self, dt):
        """
        Update all children of this layer per step

        Note the form of self.children is [(index, object), (index, object), ..]
        So to call first object's update member function we call
            self.children[0][1].update(dt)
        """
        # There has got to be some internal clock I can use...
        self.time += 1

        # Check collisions from last dt
        self.check_collisions()

        # Start list of objects to add
        to_add = []

        # Update objects for this dt
        to_add = self.update_objects(dt, to_add)

        # Remove objects for this dt
        to_add = self.remove_dead(to_add)

        # Spawn food every 120 frames for now
        if self.time % 120 == 0:
            self.add(food.Food(position=(random.randint(0,self.x_max), random.randint(0,self.y_max))))
        # Spawn matter if necessary
        # to_add = self.spawn_matter(to_add)

        # Add objects for this dt
        if to_add:
            for obj in to_add:
                self.add(obj)


    def check_collisions(self):
        """
        Check collisions between cells and anything else
        Objects interact if they collide and are not dead
        Should try out cocos2d collision checker in the future
        """
        for i in xrange(len(self.children)):
            if self.children[i][1].Type == 'cell':
                for j in xrange(1, len(self.children)):
                    if not self.children[i][1] == self.children[j][1]:
                        obj_1 = self.children[i][1]
                        obj_2 = self.children[j][1]
                        if not obj_1.dead and not obj_2.dead:
                            if obj_1.collides_with(obj_2):
                                obj_1.handle_collision_with(obj_2)
                                obj_2.handle_collision_with(obj_1)


    def update_objects(self, dt, to_add):
        """
        Simple loop to update all objects in game
        """
        for obj in ( i[1] for i in self.children):
            obj.update(dt)


    def remove_dead(self, to_add):
        """
        Remove objects that are dead
        """
        for to_remove in (i[1] for i in self.children if i[1].dead):
            # This adds anything the dead object leaves behind before it is removed
            #to_add.extend(to_remove.new_obj)
            # This takes objects off self.children tuple, and updates objects' tuples
            self.remove(to_remove)
            # This calls the dead object's deconstructor, and it ceases to exist from this point on
            to_remove.delete()
        return to_add


    def remove(self, child):
        """
        Update children list in each relevant object as well
        """
        super(SpriteLayer, self).remove(child)
        for obj in ( i[1] for i in self.children):
            # TODO: Check an object Boolean variable instead of Type
            if obj.Type == 'cell':
                obj.get_objlist(self.children)

    def add(self, child):
        """
        Update children list in each relevant object as well
        """
        super(SpriteLayer, self).add(child)
        for obj in ( i[1] for i in self.children):
            if obj.Type == 'cell':
                obj.get_objlist(self.children)

