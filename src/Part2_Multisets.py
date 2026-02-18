import random
from collections import Counter

class Part2_Multisets:
  def __init__(self):
    self.items = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
    self.n = 12
    self.bag_a = self.generate_random_bag()
    self.bag_b = self.generate_random_bag()
  
  def generate_random_bag(self):
    
    # Two items must have multiplicity 2 or more 
    force_items = random.sample(self.items, 2)
    bag = Counter({forced_items[0]: random.randint(2, 4), forced_items[1]: random.randint(2, 4)})
    
    # Fill the rest of the bag to n >= 10
    remaining_slots = self.n - sum(bag.values())
  
    if remaining_slots > 0:
      bag.update(random.choices(items, k=remaining_slots))
        
    return bag
  
