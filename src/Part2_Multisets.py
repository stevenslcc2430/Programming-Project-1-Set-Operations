"""
Team #5

Team Members
- Steven Benjamin
- Alex Gonzalez
- Carlos Recinos

CS-2430-502
Project 1: Set Operations
"""

import random
from collections import Counter

class Part2_Multisets:
    def __init__(self):
        self.items = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
        self.n = 12
        self.bag_a = self.generate_random_bag()
        self.bag_b = self.generate_random_bag()
        
        # Multiset Union (A ∪ B)
        # Takes the max count for each element
        self.union_ab = self.bag_a | self.bag_b

        # Intersection (A ∩ B)
        # Takes the minimum count for each element
        self.intersection_ab = self.bag_a & self.bag_b

        # Difference (A - B)
        # Subtracts counts of B from A without becoming negative
        self.difference_ab = self.bag_a - self.bag_b

        # Multiset Sum
        # Adds the counts together; combines the bags
        self.sum_ab = self.bag_a + self.bag_b

    def generate_random_bag(self):
        force_items = random.sample(self.items, 2)
        bag = Counter({force_items[0]: random.randint(2, 4), force_items[1]: random.randint(2, 4)})

        remaining_slots = self.n - sum(bag.values())

        if remaining_slots > 0:
            bag.update(random.choices(self.items, k=remaining_slots))

        return bag

    def display_bags(self):
        #Display both bags with their counts
        print("\n" + "=" * 60)
        print("BAG A (Multiset A):")
        print("=" * 60)
        for item, count in sorted(self.bag_a.items()):
            print(f"  {item}: {count}")
        print(f"Total items in Bag A: {self.bag_a.total()}")
        
        #same as set A
        print("\n" + "=" * 60)
        print("BAG B (Multiset B):")
        print("=" * 60)
        for item, count in sorted(self.bag_b.items()):
            print(f"  {item}: {count}")
        print(f"Total items in Bag B: {self.bag_b.total()}")

        print("=" * 100)
        print(f"{'Operation':<25} | {'Multiset Representation (Item: Count)'}")
        print(f"{'A ∪ B -  Multiset Union':<25} | {dict(self.union_ab)}")
        print(f"{'A ∩ B -  Intersection':<25} | {dict(self.intersection_ab)}")
        print(f"{'A - B -  Difference':<25} | {dict(self.difference_ab)}")
        print(f"{'A + B -  Sum':<25} | {dict(self.sum_ab)}")
# Create and use the multiset class
if __name__ == "__main__":
    # Create an instance
    multisets = Part2_Multisets()
    multisets.display_bags()
