import cocos
from cocos.director import director
from game import spritelayer

import pyglet


class Mouse(cocos.layer.Layer):

    # If you want that your layer receives events
    # you must set this variable to 'True',
    # otherwise it won't receive any event.
    is_event_handler = True

    def __init__(self):
        super( Mouse, self ).__init__()

        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy )
        self.add( self.text )

    def update_text (self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy


    def on_mouse_motion (self, x, y, dx, dy):
        """This function is called when the mouse is moved over the app.

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        #self.update_text (x, y)
        pass

    def on_mouse_press (self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
           (values like 'SHIFT', 'OPTION', 'ALT')
        """
        # Check to see if a game entity has been clicked
        pass



        #self.posx, self.posy = director.get_virtual_coordinates (x, y)
        #self.update_text (x,y)

