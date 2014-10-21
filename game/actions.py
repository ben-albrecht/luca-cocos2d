import cocos

class Eat(object):
    """
    Eat Action
    """
    def __init__(self, prey, *args, **kwargs):
        """
        Declare the prey
        """
        self.prey = prey


    def done(self):
        """
        We are done if our prey is dead, or ceases to exist
        More advanced eating may involve finishing earlier
        and fleeing if a threat becomes noticed nearby (e.g. a predator)
        """
        return self.prey.dead or self.prey == None

