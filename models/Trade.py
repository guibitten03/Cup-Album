from datetime import datetime

from models import *


class Trade(Entity):

    def __init__(self,colr1 : Collector, stk1: Sticker,
                      colr2 : Collector, stk2: Sticker, date: str="", **kwargs):
        super().__init__(Trade,**kwargs)
        self.colr1 = colr1
        self.colr2 = colr2
        self.stk1 = stk1
        self.stk2 = stk2
        self.date = date if date != "" else datetime.now().strftime("%d/%m/%Y")

    def get_colr1(self) -> Collector:
        return self.colr1

    def get_colr2(self) -> Collector:
        return self.colr2

    def get_stk1(self) -> Sticker:
        return self.stk1

    def get_stk2(self) -> Sticker:
        return self.stk2

    def get_date(self) -> str:
        return self.date

    def set_colr1(self,colr1: int) -> None:
        self.colr1 = colr1

    def set_colr2(self,colr2: int) -> None:
        self.colr2 = colr2

    def set_stk1(self,stk1: int) -> None:
        self.stk1 = stk1

    def set_stk2(self,stk2: int) -> None:
        self.stk2 = stk2

    def __str__(self):
        return "Id: {} | {} | Collector1: {} | Sticker1: {} | Collector2: {} | Sticker2: {}" \
            .format(self.id, self.date, self.colr1, self.stk1, self.colr2, self.stk2)