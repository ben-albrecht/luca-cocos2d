#!/usr/bin/env python

import cocos

from cocos import director, scene, layer
from game import  resources, menu, gameview, colors
#from game.inputs import keydisplay, mousedisplay

def main():
    """
    Every program needs a main function. This is it.
    """

    # Instantiate and Initialize main director
    maindirector = director.director
    maindirector.init(resizable=True)

    # Instantiate main scene
    mainscene = scene.Scene()

    # Instantiate main menu layer - main menu at start of game
    mainmenulayer = menu.MainMenu()

    # Instantiate gameview, a CocosNode containing layers for actual gameplay
    maingameview = gameview.GameView()

    # Add our layers in a multiplex (only 1 layer per multiplex can be visible at a time)
    # The default visible layer is the first in the multiplex (mainmenu)
    # This multiplex layer is indexed z = 1
    mainscene.add( layer.base_layers.MultiplexLayer(mainmenulayer,
                                                maingameview),
                                                z=1)

    # Instantiate background layer - just a colored layer
    #   Note: The * (splat operator) unpacks the tuple returned by rgba()
    backgroundlayer = layer.ColorLayer(*colors.rgba(colors.base3))

    # Add background, always visible, indexed at z = 0
    mainscene.add( backgroundlayer, z=0)


    # DEBUG - shows what key is pressed and mouse coords
    # scene.add( mousedisplay.MouseDisplay(), z = 2)
    # scene.add( keydisplay.KeyDisplay(), z = 3)


    # Tell director to run our scene (start game!)
    maindirector.run( mainscene )


if __name__ == "__main__":
    main()
