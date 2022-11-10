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
    If you are loading an object from the persistence memory, use the keyword argument 'id' to set its id.\n

    Example
    -------
    >>> class Foo(Entity):
    ...     def __init__(self, **kwargs) -> None:
    ...         super().__init__(Foo, **kwargs)
    ...
    ...     def __str__(self) -> str:
    ...         return str(self.get_id())
    ...
    >>> class Bar(Entity):
    ...     def __init__(self,  **kwargs) -> None:
    ...         super().__init__(Bar, **kwargs)
    ...
    ...     def __str__(self) -> str:
    ...         return str(self.get_id())
    ...
    >>> objs = [ Foo(), Foo(), Bar(), Bar(), Foo(id=25) ]
    >>> for obj in objs:
    ...     print(obj.get_id())
    0 1 0 1 25

    Temporary Entity
    ----------------
    The Entity class can be instantiated with an invalid id of minus one by passing 'unidentified = True' in the kwargs.

    Example
    -------
    >>> obj = Foo(unidentified = True)
    >>> print(obj.get_id())
    -1
    """
    id_per_type = defaultdict(int)

    @abstractmethod
    def __init__(self, t: Type, **kwargs) -> None:
        if 'id' in kwargs:
            self.id = kwargs['id']
            Entity.id_per_type[t] = max(Entity.id_per_type[t], self.id + 1)
            return

        if kwargs.get('unidentified', False):
            self.id = -1
            return

        self.id = Entity.id_per_type[t]
        Entity.id_per_type[t] = Entity.id_per_type[t] + 1

    @abstractmethod
    def __str__(self) -> str:
        pass

    def get_id(self) -> int:
        return self.id
