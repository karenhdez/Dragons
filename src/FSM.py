


class FSM(object):

    def __init__(self):

        self.main = self.state_one


    def setState(self, name):

        self.main = getattr(self, name)


    def state_one(self, args):

        pass


    def state_two(self, args):

        self.main = self.state_one