import pyglet, math, Tkinter, sys


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return  ((point_1[0] - point_2[0]) ** 2 + \
            (point_1[1] - point_2[1]) ** 2)


def distance_x(point_1=(0, 0), point_2=(0, 0)):
    """Returns the x distance between two points"""
    return  (point_1[0] - point_2[0])


def distance_y(point_1=(0, 0), point_2=(0, 0)):
    """Returns the y distance between two points"""
    return  (point_1[1] - point_2[1])


def center_image(image):
    """Sets an image to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


def get_dimensions():
    """
    Get dimensions of monitor
    I don't think I need this for Cocos2d
    """
    # TODO: test on Mac & Windows
    if sys.platform == 'darwin':
        # Mac
        #print NSScreen.mainScreen().frame()
        #dim
        #NSScreen.mainScreen().frame().width
        #NSScreen.mainScreen().frame().height
        # macbookpro 13'' =1280x800 (640, 400)
        dim = [1280, 800]
    else:
        # Linux
        t = Tkinter.Tk()
        t.attributes("-alpha", 00)
        t.attributes('-fullscreen', True)
        t.update()
        dim = [t.winfo_width(), t.winfo_screenheight()]
        t.destroy()
    return dim


def module_exists(module_name):
    """
    Check that module exists, if not, throw an error
    """
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


def record():
    """
    TODO
    Take screenshots every step (= some integer number of frames)
    Would I call my own scheduler for this?
    """
    pass
    # One Screen Shot: on key press - start, stop
    #import time
    #pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot-%d.png' % (int( time.time() ) ) )

