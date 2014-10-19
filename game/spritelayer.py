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
        self.time = 0

        # Superclass constructor
        super(SpriteLayer, self ).__init__(*args, **kwargs)

        x, y = director.get_window_size()
        self.x_max = x
        self.y_max = y
        print "Game Dimensions: ", self.x_max,"x", self.y_max

        self.load()

        # Call update function every frame
        self.schedule(self.update)


    def load(self):
        self.add(cell.Cell(position=(300,300), color=colors.blue))
        self.add(cell.Cell(position=(300,300), color=colors.blue))
        self.add(cell.Cell(position=(300,300), color=colors.blue))
        #self.children[0][1].get_objlist(self.children)

        #self.add(cell.Cell(position=(300,200), color=colors.blue))
        self.add(food.Food(position=(random.randint(250,350), random.randint(250,350))))
        self.add(food.Food(position=(random.randint(250,350), random.randint(250,350))))
        #self.add(food.Food(position=(random.randint(0, x), random.randint(0,y))))
        """
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
        self.time += 1
        # Spawn food every 120 frames for now
        if self.time % 120 == 0:
            self.add(food.Food(position=(random.randint(0,self.x_max), random.randint(0,self.y_max))))

        # Check collisions from last dt
        self.check_collisions()

        # Start list of objects to add
        to_add = []

        # Update objects for this dt
        to_add = self.update_objects(dt, to_add)

        # Remove objects for this dt
        to_add = self.remove_objects(to_add)

        # Spawn matter if necessary
        # to_add = self.spawn_matter(to_add)

        # Add objects for this dt
        if to_add:
            for obj in to_add:
                self.add(obj)


    def check_collisions(self):
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
        for obj in ( i[1] for i in self.children):
            if obj.Type == 'cell':
                obj.get_objlist(self.children)
            obj.update(dt)


    def remove_objects(self, to_add):
        for to_remove in (i[1] for i in self.children if i[1].dead):
             #to_add.extend(to_remove.new_obj)
             self.remove(to_remove)
             to_remove.delete()
        return to_add


