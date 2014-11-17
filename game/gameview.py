from cocos import  cocosnode
from game import spritelayer, menu, controllayer, hudlayer

"""
Director            Main Director
                        |
Scene(s)            Main Scene
                        |----------------------------------------
                        |                                       |
Node(s)             GameView || MainMenu                        |
                        |                                       |
              ---------------------------------                 |
              |               |               |                 |
Layers        SpriteLayer     ControlLayer    HUDLayer          BackgroundLayer
"""


class GameView( cocosnode.CocosNode ):
    def __init__(self):
        super(GameView, self).__init__()
        self.spritelayer = spritelayer.SpriteLayer()
        self.hudlayer = hudlayer.HUDLayer()
        self.controllayer = controllayer.ControlLayer()

        self.add(self.spritelayer)
        self.add(self.hudlayer)
        self.add(self.controllayer)

        self.controllayer.begin()
        self.hudlayer.begin()

