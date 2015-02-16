import cocos
from cocos import director, scene, layer
from game import  resources, menu, gameview, colors
#from game.inputs import keydisplay, mousedisplay

if __name__ == "__main__":
    """
    Main function of game
    """
    # Instantiate and Initialize main director
    director = director.director
    director.init(resizable=True)


    # Instantiate main scene
    scene = scene.Scene()

    # Instantiate main menu layer - main menu at start of game
    mainmenulayer = menu.MainMenu()

    # Instantiate gameview, a CocosNode containing layers for actual gameplay
    gameview = gameview.GameView()

    # Add our layers in a multiplex (only 1 layer per multiplex can be visible at a time)
    # The default visible layer is the first in the multiplex (mainmenu)
    # This multiplex layer is indexed z = 1
    scene.add( layer.base_layers.MultiplexLayer(
                                                    mainmenulayer,
                                                    gameview
                                                    ),
                                                 z=1)

    # Instantiate background layer - just a colored layer
    #   Note: The * (splat operator) unpacks the tuple returned by rgba()
    backgroundlayer = layer.ColorLayer(*colors.rgba(colors.base3))

    # Add background, always visible, indexed at z = 0
    scene.add( backgroundlayer, z=0)


    # DEBUG - shows what key is pressed and mouse coords
    # scene.add( mousedisplay.MouseDisplay(), z = 2)
    # scene.add( keydisplay.KeyDisplay(), z = 3)


    # Tell director to run our scene (start game!)
    director.run( scene )



