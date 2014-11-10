import cocos
from cocos.menu import *
import pyglet
from pyglet import gl, font
from pyglet.window import key
from game.colors import *
import random


from cocos.layer import *
from cocos.text import *
from cocos.actions import *
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


class ScoreLayer( Layer ):
    def __init__(self):
        w,h = director.get_window_size()
        super( ScoreLayer, self).__init__()

        # transparent layer
        self.add( ColorLayer(32,32,32,32, width=w, height=48),z=-1 )

        self.position = (0,h-48)

        self.score=  Label('Score:', font_size=36,
                font_name='Edit Undo Line BRK',
                color=(255,255,255,255),
                anchor_x='left',
                anchor_y='bottom')
        self.score.position=(0,0)
        self.add( self.score)

        self.lines=  Label('Lines:', font_size=36,
                font_name='Edit Undo Line BRK',
                color=(255,255,255,255),
                anchor_x='left',
                anchor_y='bottom')
        self.lines.position=(235,0)
        self.add( self.lines)

        self.lvl=  Label('Lvl:', font_size=36,
                font_name='Edit Undo Line BRK',
                color=(255,255,255,255),
                anchor_x='left',
                anchor_y='bottom')

        self.lvl.position=(450,0)
        self.add( self.lvl)

    def draw(self):
        super( ScoreLayer, self).draw()
        self.score.element.text = 'Score:%d' % 10
        self.lines.element.text = 'Lines:%d' % 5 #max(0, (status.level.lines - status.lines))

        #lvl = status.level_idx or 0
        lvl = 0
        self.lvl.element.text = 'Lvl:%d' % lvl

        #if status.next_piece:
        #    status.next_piece.draw()
