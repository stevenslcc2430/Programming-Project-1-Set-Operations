import random
from collections import Counter

class Part2_Multisets:
    def __init__(self):
        self.items = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
        self.n = 12
        self.bag_a = self.generate_random_bag()
        self.bag_b = self.generate_random_bag()

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
        print(f"Total items in Bag A: {sum(self.bag_a.values())}")
        #same as set A
        print("\n" + "=" * 60)
        print("BAG B (Multiset B):")
        print("=" * 60)
        for item, count in sorted(self.bag_b.items()):
            print(f"  {item}: {count}")
        print(f"Total items in Bag B: {sum(self.bag_b.values())}")

        print("\n" + "=" * 60)
        print("OPERATIONS")
        print("=" * 60)
        print(f"{'Max Count':<25} | {dict(Counter(multisets.bag_a | multisets.bag_b))}")
        print(f"{'Min Count':<25} | {dict(Counter(multisets.bag_a & multisets.bag_b))}")
        print(f"{'Difference of Multisets':<25} | {dict(Counter(multisets.bag_a - multisets.bag_b))}")
        print(f"{'Sum of MultiSers':<25} | {dict(Counter(multisets.bag_a + multisets.bag_b))}")
# Create and use the multiset class
if __name__ == "__main__":
    # Create an instance
    multisets = Part2_Multisets()
    multisets.display_bags()
