import random

class Part1_OrdinarySets:

	universal = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
	n = len(universal)

	# random.choice to create subsets of universal set
	bool_a = [random.choice([True, False]) for _ in range(n)]
	bool_b = [random.choice([True, False]) for _ in range(n)]
  
