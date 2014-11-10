import cocos
from cocos.menu import *
import pyglet
from pyglet import gl, font
from pyglet.window import key
from game.colors import *
import random

class MainMenu( cocos.menu.Menu ):
    """
    Main menu that player sees first when game starts
    """
    def __init__(self):
        super( MainMenu, self).__init__('LUCA')

        #self.select_sound = soundex.load('move.mp3')

        # you can override the font that will be used for the title and the items
        # you can also override the font size and the colors. see menu.py for
        # more info
        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 72
        self.font_title['color'] = rgba(base03)

        self.font_item['font_name'] = 'Edit Undo Line BRK',
        self.font_item['color'] = rgba(base03)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Edit Undo Line BRK'
        self.font_item_selected['color'] = rgba(color[random.randint(0,7)])
        self.font_item_selected['font_size'] = 46


        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        items.append( MenuItem('New Game', self.on_new_game) )
        #items.append( MenuItem('Options', self.on_options) )
        #items.append( MenuItem('Scores', self.on_scores) )
        items.append( MenuItem('Quit', self.on_quit) )

        self.create_menu( items, shake(), shake_back() )


    def on_new_game(self):
        self.parent.switch_to(1)

    def on_options( self ):
        # This used to be new game... need to figure out how this works
        import gameview
        director.push( FlipAngular3DTransition(
            gameview.get_newgame(), 1.5 ) )


    #def on_scores( self ):
    #    self.parent.switch_to(2)

    def on_quit(self):
        pyglet.app.exit()



class SideMenu( cocos.menu.Menu ):
    """
    Menu on the side of game for information and interaction with game
    WORK IN PROGRESS
    """
    def __init__(self):
        super( SideMenu, self).__init__('LUCA')

        x,y = cocos.director.director.get_window_size()
        x = x - 0.25*x
        self._set_position((x, y))
        self._set_scale_x(0.25)

        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 72
        self.font_title['color'] = rgba(base03)

        self.font_item['font_name'] = 'Edit Undo Line BRK',
        self.font_item['color'] = rgba(base03)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Edit Undo Line BRK'
        self.font_item_selected['color'] = rgba(color[random.randint(0,7)])
        self.font_item_selected['font_size'] = 46


        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        # items.append( MenuItem('New Game', self.on_new_game) )
        #items.append( MenuItem('Options', self.on_options) )
        #items.append( MenuItem('Scores', self.on_scores) )
        items.append( MenuItem('Quit', self.on_quit) )

        self.create_menu( items, shake(), shake_back() )


    def on_new_game(self):
        self.parent.switch_to(1)

    def on_options( self ):
        # This used to be new game... need to figure out how this works
        import gameview
        director.push( FlipAngular3DTransition(
            gameview.get_newgame(), 1.5 ) )


    #def on_scores( self ):
    #    self.parent.switch_to(2)

    def on_quit(self):
        pyglet.app.exit()
