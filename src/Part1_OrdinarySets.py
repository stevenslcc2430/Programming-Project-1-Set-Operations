import random

class Part1_OrdinarySets:
	def __init__(self):
		self.universal = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
		self.n = len(self.universal)

	# random.choice to create subsets of universal set
	bool_a = [random.choice([True, False]) for _ in range(self.n)]
	bool_b = [random.choice([True, False]) for _ in range(self.n)]
  
