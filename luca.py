import cocos
from game import keydisplay, mousedisplay, resources, spritelayer


if __name__ == "__main__":
    # Instantiate main director
    Main = cocos.director.director

    # Initialize main cocos director (window)
    Main.init(resizable=True)

    # Run a scene with our event displayers:
    Main.run( cocos.scene.Scene( spritelayer.SpriteLayer() ) )

    # Sample of running multiple scenes at once:
    #cocos.director.director.run( cocos.scene.Scene( keydisplay.KeyDisplay(), mousedisplay.MouseDisplay(), MainLayer() ) )


