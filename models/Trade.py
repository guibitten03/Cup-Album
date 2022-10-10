from datetime import datetime
from models.Entity import Entity

class Trade(Entity):

    def __init__(self,collector1 : str, sticker1: int,
                      collector2 : str, sticker2: int, date: str="", **kwargs):
        super().__init__(Trade,**kwargs)
        self.collector1 = collector1
        self.collector2 = collector2
        self.sticker1 = sticker1
        self.sticker2 = sticker2
        self.date = date if date != "" else datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def get_id(self) -> str:
        return self.id
    def get_collector1(self) -> str:
        return self.collector1
    def get_collector2(self) -> str:
        return self.collector2
    def get_sticker1(self) -> str:
        return self.sticker1
    def get_sticker2(self) -> str:
        return self.sticker2
    def get_date(self) -> str:
        return self.date

    def set_collector1(self,collector1: str) -> None:
        self.collector1 = collector1
    def set_collector2(self,collector2: str) -> None:
        self.collector2 = collector2
    def set_sticker1(self,sticker1: int) -> None:
        self.sticker1 = sticker1
    def set_sticker2(self,sticker2: int) -> None:
        self.sticker2 = sticker2
    
    def __str__(self):
        return "Id: {}, {}, Collector1: {}, Sticker1: {}, Collector2: {}, Sticker2: {}".format(
                self.id,self.date, self.collector1,self.sticker1,self.collector2,self.sticker2)