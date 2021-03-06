import pyglet
import random
from pyglet import gl, font
from pyglet.window import key
from cocos import layer, menu, text, director
from game import colors

class MainMenu( menu.Menu ):
    """
    Main menu that player sees first when game starts
    """
    def __init__(self):
        super( MainMenu, self).__init__('LUCA')

        #self.select_sound = soundex.load('move.mp3')

        # you can override the font that will be used for the title and the items
        # you can also override the font size and the colors. see menu.py for
        # more info
        #self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 72
        self.font_title['color'] = colors.rgba(colors.base03)

        self.font_item['font_name'] = 'Edit Undo Line BRK',
        self.font_item['color'] = colors.rgba(colors.base03)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Edit Undo Line BRK'
        self.font_item_selected['color'] = colors.rgba(colors.color[random.randint(0,7)])
        self.font_item_selected['font_size'] = 46


        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = menu.CENTER
        self.menu_anchor_x = menu.CENTER

        items = []

        items.append( menu.MenuItem('New Game', self.on_new_game) )
        #items.append( MenuItem('Options', self.on_options) )
        #items.append( MenuItem('Scores', self.on_scores) )
        items.append( menu.MenuItem('Quit', self.on_quit) )

        self.create_menu( items, menu.shake(), menu.shake_back() )


    def on_new_game(self):
        self.parent.switch_to(1)

    def on_options( self ):
        # This used to be new game... need to figure out how this works
        #import gameview
        director.director.push( FlipAngular3DTransition(
            gameview.get_newgame(), 1.5 ) )


    #def on_scores( self ):
    #    self.parent.switch_to(2)

    def on_quit(self):
        pyglet.app.exit()


