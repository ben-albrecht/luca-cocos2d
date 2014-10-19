import cocos
from game import  resources, spritelayer
from game.inputs import keydisplay, mousedisplay
from game import menu
from game.colors import *


if __name__ == "__main__":
    # Instantiate main director
    director = cocos.director.director

    # Initialize main cocos director (window)
    director.init(resizable=True)
    scene = cocos.scene.Scene()


    # Run a scene with our event displayers:
    spritelayer = spritelayer.SpriteLayer()
    backgroundlayer = cocos.layer.ColorLayer(base3[0], base3[1], base3[2], 255)

    scene.add( cocos.layer.base_layers.MultiplexLayer(
                                                    menu.MainMenu(),
                                                    spritelayer
                                                    ),
                                                 z=1)
    scene.add( backgroundlayer, z=0)

    director.run( scene )

    # Sample of running multiple scenes at once:
    #cocos.director.director.run( cocos.scene.Scene( keydisplay.KeyDisplay(), mousedisplay.MouseDisplay(), MainLayer() ) )

"""
    pyglet.resource.path.append('data')
    pyglet.resource.reindex()
    font.add_directory('data')

    director.init( resizable=True, width=600, height=720 )
    scene = Scene()
    scene.add( MultiplexLayer(
                    MainMenu(),
                    OptionsMenu(),
                    ScoresLayer(),
                    ),
                z=1 )
    scene.add( BackgroundLayer(), z=0 )
    director.run( scene )
"""
