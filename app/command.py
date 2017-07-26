command_list = {}


class Command:
    """
    Represent command in system
    """
    def __init__(self, name, description='', in_help=True):
        self.name = name.lower()
        self.in_help = in_help
        self.description = description
        self.__keys = [self.name]
        command_list.append(self)

    @property
    def keys(self):
        return self.__keys.copy()

    @keys.setter
    def keys(self, lst):
        self.__keys += [i.lower() for i in lst]

    def process(self, obj):
        # Function to handle message
        pass