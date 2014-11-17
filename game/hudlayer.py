import pyglet
import random
from pyglet import gl, font
from pyglet.window import key
from cocos import layer, menu, text, director
from game import colors

class HUDLayer( layer.Layer ):
    """
    Heads-Up Display on side of screen during game
    Displays information and contains menus
    """

    def __init__(self):
        w,h = director.director.get_window_size()
        super( HUDLayer, self).__init__()

        # transparent layer
        self.add( layer.ColorLayer(32,32,32,32, width=192, height=h),z=-1 )

        self.position = (w - 192, 0)

        self.counter = text.Label('organisms', font_size=12,
                        color=colors.rgba(colors.base03),
                        anchor_x='left',
                        anchor_y='bottom')

        self.counter.position=(0, h-50)
        self.add( self.counter)


    def begin(self):
        """
        Called after instantiated and added to scene to get parent data
        """
        self.spritelayer = self.parent.spritelayer


    def draw(self):
        super( HUDLayer, self).draw()
        self.counter.element.text = 'Organisms:%d' % len(self.spritelayer.children)
        #self.lines.element.text = 'Lines:%d' % 5 #max(0, (status.level.lines - status.lines))

        #lvl = status.level_idx or 0
        #lvl = 0
        #self.lvl.element.text = 'Lvl:%d' % lvl

        #if status.next_piece:
        #    status.next_piece.draw()
