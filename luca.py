import cocos
from game import  resources, spritelayer
from game.inputs import keydisplay, mousedisplay
from game import menu
from game.colors import *

if __name__ == "__main__":
    """
    Main function of game
    """
    # Instantiate and Initialize main director
    director = cocos.director.director
    director.init(resizable=True)

    # Instantiate main scene
    scene = cocos.scene.Scene()

    # Instantiate sprite layer - layer with all the sprite objects
    spritelayer = spritelayer.SpriteLayer()

    # Instantiate background layer - just a colored layer
    backgroundlayer = cocos.layer.ColorLayer(base3[0], base3[1], base3[2], 255)

    # Instantiate main menu layer - main menu at start of game
    mainmenulayer = menu.MainMenu()

    # Add our layers in a multiplex (only 1 layer per multiplex can be visible at a time)
    # The default visible layer is the first in the multiplex (mainmenu)
    # This multiplex layer is indexed z = 1
    scene.add( cocos.layer.base_layers.MultiplexLayer(
                                                    mainmenulayer,
                                                    spritelayer
                                                    ),
                                                 z=1)
    # Add background, always visible, indexed at z = 0
    scene.add( backgroundlayer, z=0)

    # DEBUG - shows what key is pressed and mouse coords
    # scene.add( mousedisplay.MouseDisplay(), z = 2)
    # scene.add( keydisplay.KeyDisplay(), z = 3)

    # Tell director to run our scene (start game!)
    director.run( scene )
