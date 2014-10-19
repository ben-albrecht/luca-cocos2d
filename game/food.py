import cocos
from game import physicalobject, colors, resources


class Food(physicalobject.PhysicalObject):
    """
    Food for the cells!
    """
    def __init__(self, *args, **kwargs):
        """
        Food constructor
        """
        super(Food, self).__init__(resources.cell_image, color=colors.base02, *args, **kwargs)
        self.Type = 'food'


    def handle_collision_with(self, other_object):
        if other_object.Type == 'cell':
            if other_object.energy < other_object.energy_max-5:
                if self.scale < 0.2:
                    self.dead = True
                else:
                    self.scale += -0.1

