import cocos


#class Eat(cocos.actions.base_actions.Action):
class Eat(object):
    def __init__(self, prey, *args, **kwargs):
        self.prey = prey


    def done(self):
        return self.prey.dead or self.prey == None

