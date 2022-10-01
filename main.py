from models.Collector import Collector
from persistence.Collector_Persistence import CollectorPersistence


def main():
	CollectorPersistence.load()
	c1 = Collector("yan0")
	c2 = Collector("yan1")
	c3 = Collector("yan2")
	c4 = Collector("yan3")
	CollectorPersistence.insert(c1)
	CollectorPersistence.insert(c2)
	CollectorPersistence.insert(c3)
	CollectorPersistence.insert(c4)
	CollectorPersistence.view_data()
	CollectorPersistence.save()

	pass

if __name__ == '__main__':
	main()