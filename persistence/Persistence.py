from abc import ABC, abstractmethod


class IPersistence(ABC):
	
	@abstractmethod
	def insert():
		pass

	@abstractmethod
	def modify():
		pass

	@abstractmethod
	def delete():
		pass

	@abstractmethod
	def search_by_id(id: int):
		pass

	@abstractmethod
	def search_by_str(s: str):
		pass