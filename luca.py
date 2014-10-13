import cocos
from game import keydisplay, mousedisplay, resources

class Cell(cocos.sprite.Sprite):
    def __init__(self, *args, **kwargs ):
        super(Cell, self).__init__(*args, **kwargs)


class SpriteLayer( cocos.layer.Layer ):
    is_event_handler = True     #: enable pyglet's events
    def __init__( self, index=1 ):
        super(SpriteLayer, self ).__init__()
        self.index = index

        self.image = resources.cell_image
        #self.image = pyglet.resource.image('grossini.png')
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.cell = cocos.sprite.Sprite(self.image)
        self.add(self.cell)
        self.cell.position = 100,200
        #self.cell.draw()






if __name__ == "__main__":
    a=1
    # Initialize a cocos director (window)
    Main = cocos.director.director
    Main.init(resizable=True)
    # Run a scene with our event displayers:
    #cocos.director.director.run( cocos.scene.Scene( keydisplay.KeyDisplay(), mousedisplay.MouseDisplay(), MainLayer() ) )
    Main.run( cocos.scene.Scene( SpriteLayer() ) )
    #print Main.fake_time


