from models.Entity import Entity


class Collector(Entity):

    def __init__(self,name : str, **kwargs):
        super().__init__(Collector,**kwargs)
        self.name = name

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def set_name(self,name : str):
        self.name = name

    def __str__(self):
        return "Id: {}, Name: {}".format(self.id, self.name)
