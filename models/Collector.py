from models import Entity

class Collector(Entity):

    def __init__(self, name: str, **kwargs):
        super().__init__(Collector,**kwargs)

        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def __str__(self):
        return "Id: {}| Name: {}".format(self.get_id(), self.name)
