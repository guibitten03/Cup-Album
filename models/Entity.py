from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Type


class Entity(ABC):
    """
    Description
    -----------
    Entity represents the base class of the system.
    It can not be instatiated and should be inherited by all classes in the models package.
    It is responsable for setting the id of each object instantiated.\n
    The id is class related, so objects of differents class may have same id.
    If you are loading an object from the persistence memory, use the keyword argument 'id' to set its id.
    Example
    -------
    >>> class Foo(Entity):
    ...	def __init__(self) -> None:
    ...		super().__init__(Foo)
    >>> class Bar(Entity):
    ...	def __init__(self) -> None:
    ...		super().__init__(Bar)
    >>> objs = [ Foo(), Foo(), Bar(), Bar() ]
    >>> for obj in objs:
    ...	print(obj.get_id())
    0 1 0 1
    """
    id_per_type = defaultdict(int)

    @abstractmethod
    def __init__(self, t: Type, **kwargs) -> None:
        if 'id' in kwargs:
            self.id = kwargs['id']
            Entity.id_per_type[t] = max(Entity.id_per_type[t], self.id + 1)
        else:
            self.id = Entity.id_per_type[t]
            Entity.id_per_type[t] = Entity.id_per_type[t] + 1

    @abstractmethod
    def __str__(self) -> str:
        pass

    def get_id(self) -> int:
        return self.id