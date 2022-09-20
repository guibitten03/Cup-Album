from abc import ABC, abstractmethod

class Entity(ABC):
	id: int = 0

	@abstractmethod
	def __init__(self) -> None:
		self.id = Entity.id
		Entity.id = Entity.id + 1

	@abstractmethod
	def __str__() -> str:
		pass
