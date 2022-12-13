from controle import Controle
from persistence.Collector_Persistence import CollectorPersistence

class CollectorControle(Controle):

    def __init__(self) -> None:
        super().__init__(CollectorPersistence())