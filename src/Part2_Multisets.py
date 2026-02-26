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
        bag = Counter({force_items[0]: random.randint(2, 4), force_items[1]: random.randint(2, 4)})
        # Fill the rest of the bag to n >= 10
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

        #MAXIMUM/MINIMUM COUNTS
    def get_max_min_counts(self):
        #Find the maximum and minimum count for each element across both sets. Returns a dictionary with each item's max and min count.
        result = {} #store output
        # Get all unique items from both bags by using set() to remove duplicates
        all_items = set(self.bag_a.keys()) | set(self.bag_b.keys())
        #use all items to get values in both sets and get count for element using for loop
        for item in sorted(all_items):
            count_a = self.bag_a.get(item, 0)  # Get count from bag A (0 if not present)
            count_b = self.bag_b.get(item, 0)  # Get count from bag B (0 if not present)
            #get results by adding/subtracting counts
            result[item] = {
                'max': max(count_a, count_b),
                'min': min(count_a, count_b),
                'count_a': count_a,
                'count_b': count_b
            }
        return result

    #SUBTRACT B'S COUNT FROM A'S COUNT
    def subtract_b_from_a(self):
        #store final answer
        result = Counter()
        # Get all unique items from both bags (reused from min_max part)
        all_items = set(self.bag_a.keys()) | set(self.bag_b.keys())
        #get count for element using for loop (also reused from min_max part)
        for item in all_items:
            count_a = self.bag_a.get(item, 0) # Get count from bag A (0 if not present)
            count_b = self.bag_b.get(item, 0) # Get count from bag A (0 if not present)

            # Subtract counts but (if negative then replace with zero)
            result[item] = max(0, count_a - count_b)

            # first if statement checks if item exits in either set(not zero/false)
            if count_a > 0 or count_b > 0:
             #this does the math(a-b) and display results with formating
                print(f"{item:10}: {count_a} - {count_b} = {result[item]} "
                      #2nd if statement is when the result is negative will print out capped at zero message
                      f"{'(capped at 0)' if count_a - count_b < 0 else ''}")
        return result
    #ADD THE COUNTS FOR EACH ELEMENT
    def add_counts(self):
       # store result
        result = Counter()
        # Get all unique items from both bags (reused again)
        all_items = set(self.bag_a.keys()) | set(self.bag_b.keys())
        #first get the count for element, then add both, store result then loop for rest of elements
        for item in sorted(all_items):
        # get count for element using for loop (also reused from min_max part)
            count_a = self.bag_a.get(item, 0) # Get count from bag A (0 if not present)
            count_b = self.bag_b.get(item, 0) # Get count from bag A (0 if not present)
            result[item] = count_a + count_b
        #display output 
            print(f"{item:10}: {count_a} + {count_b} = {result[item]}")
        return result

    def display_all_operations(self):
    #display all multiset operations
        # First show the original bags
        self.display_bags()
        #Display the maximum/minimum counts for each element
        print("\n" + "=" * 60)
        print("MAXIMUM AND MINIMUM COUNTS PER ELEMENT")
        print("=" * 60)

        counts = self.get_max_min_counts()
        #legend/key row (for the table part)
        print(f"{'Item':<12} {'Count A':<8} {'Count B':<8} {'Max':<8} {'Min':<8}")
        print("-" * 50)
        #for loop that goes through all items counted from the min/max part then also use format options to make table look readable
        for item, data in counts.items():
            print(f"{item:<12} {data['count_a']:<8} {data['count_b']:<8} "
                  f"{data['max']:<8} {data['min']:<8}")

        # label 4 new section (subtraction part)
        print("\n" + "=" * 60)
        print("SUBTRACTION: BAG A - BAG B (non-negative)")
        print("=" * 60)
        # Show subtraction (A - B)  non-negative
        subtraction_result = self.subtract_b_from_a()

        # label 4 new section (addition part)
        print("\n" + "=" * 60)
        print("ADDITION: BAG A + BAG B")
        print("=" * 60)
        # Show addition
        addition_result = self.add_counts()


# Create and use the multiset class
if __name__ == "__main__":
    # Create an instance
    multisets = Part2_Multisets()

    # Display all operations
    multisets.display_all_operations()
