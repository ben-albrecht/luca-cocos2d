from cocos import layer, director, euclid
from pyglet.window import key, mouse
import weakref

class ControlLayer( layer.ScrollingManager ):
    """
    This layer manages the controls of the game
    Mouse and Keyboard inputs only

    The special function names are recognized by pyglet
        when `is_event_handler = True`

    This results in on_* functions being called upon certain events:
        on_key_press
        on_key_release
        on_mouse_press
        on_mouse_scroll
        on_mouse_drag

    key_manager() tracks the status of keys pressed in our key_update()
    """

    is_event_handler = True

    def __init__(self):
        """
        Set some aliases for less verbose code
        """
        super(ControlLayer, self).__init__()

        # Mouse Management
        self.lastobj = None
        self.objcolor = None

        # Key Management
        self.keys_pressed = set()
        self.schedule(self.key_update)

        # Screen Management
        w, h = director.director.get_window_size()
        self.xmin = w - 10
        self.xmax = w + 10
        self.ymin = h - 10
        self.ymax = h + 10

        self.i = 0

    def begin(self):
        """
        This must be called after layer is added to scene,
        so that we have a parent defined
        """
        self.spritelayer = self.parent.spritelayer
        hudlayer = self.parent.hudlayer

        """
        proto-editor stuff
        scroller = scrolling manager
        worldview = scrollable layer
        """

        self.wwidth = self.spritelayer.width
        self.wheight = self.spritelayer.height
        self.pixel_to_screen    #world_to_screen
        self.pixel_from_screen  #screen_to_world

        self.spritelayer.camera.restore()
        self.spritelayer.x, self.spritelayer.y = 0, 0
        self.zoom_fastness = 1.0

    def key_update(self, dt):
        self.key_manager()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Check to see if a game entity has been clicked

        TODO:
            Ein Kleine Problem - x and y coordinates need to be scaled
                according to current camera zoom
            This is actually kind of hard to figure out
        """

        print(x, y)
        self.world_mouse = self.pixel_from_screen(x, y)
        x, y = self.world_mouse
        x, y = self.pixel_to_screen(x, y)
        #self.screen_mouse = self.pixel_to_screen(x, y)
        print('updated', x, y)
        if button & mouse.LEFT:

            # Account for x and y offset of spritelayer view
            #x -= self.spritelayer.x
            #y -= self.spritelayer.y

            # Will set true if object detected under mouse
            targetclicked = False

            # Undo previous click
            self.undo_click()

            #print self.spritelayer.camera.eye[2]
            #print 'screen', self.screen_mouse[0], self.screen_mouse[1]

            # Find out what was clicked
            for obj in (i[1] for i in self.spritelayer.children):
                if  obj.contains(x, y):
                    print("object:")
                    print(obj.x, obj.y)
                    targetclicked = True
                    self.lastobj = obj
                    break
            self.handle_click(targetclicked)

    def handle_click(self, targetclicked):
        """
        Handle the click that has occurred
        Note: self.lastobj = object that is clicked currently
        """

        if targetclicked == True:

            #self.lastobj.stats()
            self.objcolor = self.lastobj.color

            # Make the object clicked turn red
            self.lastobj.color = (240, 30, 30)
            #print "obj clicked"

            if not self.lastobj.Type == 'food':
                # Change to POV of this object
                self.lastobj.clicked = True

    def undo_click(self):
        """
        Undo everything that happened when we clicked
        Note: self.last = object that was clicked previously
        """
        if not self.lastobj == None and self.lastobj.dead == False:
            # Last object still exists
            self.lastobj.color = self.objcolor
            self.lastobj.clicked = False
            self.lastobj = None
        else:
            self.lastobj = None

    def on_key_press(self, symbol, modifier):
        """
        Hotkeys

        Space   -> Pause/Unpause
        R       -> Restore View
        """
        # Space pauses the objects in the game, but not HUD
        self.keys_pressed.add (symbol)

        if symbol == key.SPACE:

            # Pause main updater
            self.spritelayer.update_pause = not self.spritelayer.update_pause

            # Pause any actions of any objects
            if self.spritelayer.update_pause == True:
                for obj in (i[1] for i in self.spritelayer.children):
                    obj.pause()
            else:
                for obj in (i[1] for i in self.spritelayer.children):
                    obj.resume()

        if symbol == key.R:
            # Resets z to original value
            self.spritelayer.camera.restore()

            # Reset x and y to center
            self.spritelayer.x, self.spritelayer.y = 0, 0

    def key_manager(self):
        """
        Key manager for keys to repeat while held down
        WASD / Arrows / HJKL

        TODO: Prevent viewing out of bounds
        """
        for symbol in self.keys_pressed:
            # Camera Navigation with key arrows, WASD, and HJKL
            if symbol == key.UP or symbol == key.W or symbol == key.K:
                self.spritelayer.y += -3
            if symbol == key.DOWN or symbol == key.S or symbol == key.J:
                self.spritelayer.y += +3
            if symbol == key.RIGHT or symbol == key.D or symbol == key.L:
                self.spritelayer.x += -3
            if symbol == key.LEFT or symbol == key.A or symbol == key.H:
                self.spritelayer.x += 3

    def on_mouse_drag(self, x, y, dx, dy, button, modifier):
        """
        Drag mouse to move around map

        TODO: Prevent viewing out of bounds
        """
        if button & mouse.RIGHT or (button & mouse.LEFT and key.M in self.keys_pressed):
            self.spritelayer.set_view(self.spritelayer.view_x + dx, self.spritelayer.view_y + dy, self.spritelayer.width, self.spritelayer.height)

            #self.spritelayer.camera._set_eye(euclid.Point3(self.spritelayer.camera.eye[0] + dx,
            #                 self.spritelayer.camera.eye[1] + dy,
            #                 self.spritelayer.camera.eye[2]))

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        """
        Mouse Scrolling
        Scroll up = zoom in and vice versa
        TODO: Prevent zooming out of bounds

        """
        #print self.spritelayer.camera.eye[2]
        #print x, y

        #self.set_focus(self.wwidth, self.wheight)
        ##self.wwidth = self.spritelayer.width
        ##self.wheight = self.spritelayer.height
        #zoom = self.spritelayer.scale + -0.016666 * scroll_y
        #self.spritelayer.scale = zoom


        #self.update_zoom(scroll_y)
        self.spritelayer.camera._set_eye(euclid.Point3(self.spritelayer.camera.eye[0],
                             self.spritelayer.camera.eye[1],
                             self.spritelayer.camera.eye[2] - self.spritelayer.camera.eye[2] * scroll_y / 10 ))


    """
    proto-editor stuff
    """
    """
    def mouse_into_world(self):
        #worldview = self.weak_worldview()
        #? allow lower limits != 0 ?
        return ( (0 <= self.world_mouse[0] <= self.spritelayer.width) and
                 (0 <= self.world_mouse[1] <= self.spritelayer.height))


    def update_zoom(self, dz):
        if self.mouse_into_world():
            wzoom_center = self.world_mouse
            szoom_center = self.screen_mouse
        else:
            # decay to scroller unadorned
            wzoom_center = None
        #if self.wheel !=0:
        #    dt_dz = 0.01666666 * self.wheel
        #    self.wheel = 0
        #else:
            dt_dz = 0.01666666 * dz
        #scroller = self.weak_scroller()
        zoom = self.scale + dt_dz * self.zoom_fastness
        #if zoom < self.zoom_min:
        #    zoom = self.zoom_min
        #elif zoom > self.zoom_max:
        #    zoom = self.zoom_max
        self.scale = zoom
        #if wzoom_center is not None:
        #    # postprocess toward 'world point under mouse the same before
        #    # and after zoom' ; other restrictions may prevent fully comply
        #    wx1, wy1 = screen_to_world(*szoom_center)
        #    fx = self.restricted_fx + (wzoom_center[0] - wx1)
        #    fy = self.restricted_fy + (wzoom_center[1] - wy1)
        #    self.set_focus(fx, fy)
    """

    def on_key_release (self, symbol, modifiers):
        """
        This function is called when a key is released.

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
