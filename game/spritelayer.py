import cocos
import random
from game import resources, colors, physicalobject, cell, food
#from cocos.actions import *
from pyglet.window import key, mouse


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
        self.x_max, self.y_max = cocos.director.director.get_window_size()
        print "Game Dimensions: ", self.x_max,"x", self.y_max

        # Load objects into the game - spawns cells, food, etc.
        self.load()

        # Set up scheduler to call update function every frame
        self.schedule(self.update)

        self.update_pause = False


        # Mouse Management
        self.lastobj = None
        self.clicked_objects = []
        self.objcolor = None

        # Key Management
        self.keys_pressed = set()

        # Screen Management
        self.xmin = self.x_max - 10
        self.xmax = self.x_max + 10
        self.ymin = self.y_max - 10
        self.ymax = self.y_max + 10

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
        self.key_manager()

        if self.update_pause == True:
            return

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
        for obj in (i[1] for i in self.children):
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
        for obj in (i[1] for i in self.children):
            # TODO: Check an object Boolean variable instead of Type
            if obj.Type == 'cell':
                obj.get_objlist(self.children)

    def add(self, child):
        """
        Update children list in each relevant object as well
        """
        super(SpriteLayer, self).add(child)
        for obj in (i[1] for i in self.children):
            if obj.Type == 'cell':
                obj.get_objlist(self.children)



    def on_mouse_press(self, x, y, button, modifiers):
        """
        Check to see if a game entity has been clicked
        """
        targetclicked = False
        #self.objects = self.ObjectManager.objects
        # Find out what was clicked
        for obj in (i[1] for i in self.children):
            #if obj.hit_test(x, y):
            if  obj.contains(x, y):
                self.undo_click()
                targetclicked = True
                self.lastobj = obj
                break
        self.handle_click(targetclicked)


    def handle_click(self, targetclicked):
        """
        Handle the click that has occurred
        """
        if targetclicked == False:
            self.undo_click()
        else:

            #self.lastobj.stats()
            self.objcolor = self.lastobj.color
            self.lastobj.color = (240, 30, 30)

            if not self.lastobj.Type == 'food':
                # Change to POV of this object
                self.lastobj.clicked = True
                self.clicked = True


    def undo_click(self):
        """
        Undo everything that happened when we clicked
        """
        if not self.lastobj == None:
            #self.lastobj.batch = self.batch
            self.lastobj.color = self.objcolor
            self.lastobj.clicked = False
            self.clicked_objects = []
            self.lastobj = None


    def on_key_press(self, symbol, modifier):
        """
        Hotkeys for sprite layer
        """
        # Space pauses the objects in the game, but not HUD
        self.keys_pressed.add (symbol)

        if symbol == key.SPACE:

            # Pause main updater
            self.update_pause = not self.update_pause

            # Pause any actions of any objects
            if self.update_pause == True:
                for obj in (i[1] for i in self.children):
                    obj.pause()
            else:
                for obj in (i[1] for i in self.children):
                    obj.resume()

        if symbol == key.R:
            # Resets z to original value
            self.camera.restore()

            # Reset x and y to center
            self.x, self.y = 0, 0

    def key_manager(self):
        """
        Key manager for keys to repeat while held down
        """
        for symbol in self.keys_pressed:
            # Camera Navigation with key arrows, WASD, and HJKL
            if symbol == key.UP or symbol == key.W or symbol == key.K:
                self.y += -3
            if symbol == key.DOWN or symbol == key.S or symbol == key.J:
                self.y += +3
            if symbol == key.RIGHT or symbol == key.D or symbol == key.L:
                self.x += -3
            if symbol == key.LEFT or symbol == key.A or symbol == key.H:
                self.x += 3


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """
        Drag mouse to move around map
        """
        if buttons & mouse.LEFT:
            #if self.ymin < self.y < self.ymax:
            self.y += dy
            #if self.xmin < self.x < self.xmax:
            self.x += dx
            print self.x, self.y


    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.camera._set_eye(cocos.euclid.Point3(self.camera.eye[0],
                             self.camera.eye[1],
                             self.camera.eye[2] + self.camera.eye[2] * scroll_y / 10 ))



    def on_key_release (self, symbol, modifiers):
        """This function is called when a key is released.

        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)

        Constants are the ones from pyglet.window.key
        """
        # Supresses error output for first enter
        try:
            self.keys_pressed.remove (symbol)
        except:
            pass
