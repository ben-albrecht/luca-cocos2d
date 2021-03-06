from __future__ import print_function
import cocos
from game import util

class PhysicalObject(cocos.sprite.Sprite):
    """
    Any physical object in the game
    Will handle collision checking, collision handling, and spawning
    """
    def __init__(self, *args, **kwargs):
        if 'attributes' in kwargs:
            for key, value in kwargs['attributes'].items():
                setattr(self, key, value)
            kwargs.pop('attributes')
        super(PhysicalObject, self).__init__(*args, **kwargs)


        self.direction = 0
        self.velocity = (0, 0)
        self.x_max, self.y_max = cocos.director.director.get_window_size()
        self.x_min, self.y_min = 0, 0
        self.Type = 'null'
        self.time = 0

        # List of objects retrieved from SpriteLayer
        self.objects = []

        # SpriteLayer checks this for new objects to add
        self.new_obj = []
        # Checked in SpriteLayer to determine what to delete
        self.dead = False

    def get_objlist(self, objects):
        """
        Grab the list of objects from sprite layer
        So that the object can interact with other objects
        This gets updated before update in SpriteLayer
        """
        if not self.objects == objects:
            self.objects = objects
            # Or is it faster to just update without checking?

    def collides_with(self, other_object):
        """
        Check if object collides with another object
        TODO: Optimize more precisely - consider grid-based approach
        """
        if util.distance_x(self.position, other_object.position) <= 50:
            collision_distance = (self.image.width * 0.5 * self.scale + \
                             other_object.scale * other_object.image.width * 0.5)
            if util.distance_x(self.position, other_object.position) <= collision_distance:
                if util.distance_y(self.position, other_object.position) <= collision_distance:
                    collision_distance_squared = collision_distance ** 2
                    actual_distance_squared = util.distance(self.position, other_object.position)
                    if self.time % 10 == 0:
                        return (actual_distance_squared <= collision_distance_squared)
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def handle_collision_with(self, other_object):
        """
        Default collision handler for objects of same type
        """

        if other_object.Type == self.Type:
            # Bounce away
            if self.x <= other_object.x:
                dx = -self.image.width*0.5
            else:
                dx = self.image.width*0.5
            if self.y <= other_object.y:
                dy = -self.image.height*0.5
            else:
                dy = self.image.height*0.5
            self.set_position(self.x + dx, self.y + dy)
        else:
            pass

    def hit_test(self, x, y):
        """ Is the coordinates (x,y) within the object bounds? """
        if x < self.x + self.image.width*self.scale/2 and \
            x > self.x - self.image.width*self.scale/2 and \
            y < self.y + self.image.height*self.scale/2 and \
            y > self.y - self.image.height*self.scale/2:
                print("Object Hit!")
                return True
        else:
            return False

    def update(self, dt):
        self.time += 1
        """
        temporarily nothing
        """

    def delete(self):
        """
        Delete object
        """
        super(PhysicalObject, self).delete()

