import cocos
from game import  resources, spritelayer
from game.inputs import keydisplay, mousedisplay


if __name__ == "__main__":
    # Instantiate main director
    Main = cocos.director.director

    # Initialize main cocos director (window)
    Main.init(resizable=True)

    # Run a scene with our event displayers:
    spritelayer = spritelayer.SpriteLayer(253, 246, 227, 255)
    Main.run( cocos.scene.Scene(spritelayer) )

    # Sample of running multiple scenes at once:
    #cocos.director.director.run( cocos.scene.Scene( keydisplay.KeyDisplay(), mousedisplay.MouseDisplay(), MainLayer() ) )


