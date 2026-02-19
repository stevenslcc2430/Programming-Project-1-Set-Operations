import random


class Part1_OrdinarySets:
    def __init__(self):
        self.universal = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
        self.n = len(self.universal)

        # Create random boolean lists for two subsets
        self.bool_a = [random.choice([True, False]) for _ in range(self.n)]
        self.bool_b = [random.choice([True, False]) for _ in range(self.n)]

    def get_set_from_boolean(self, bool_list):
        #Convert boolean values to actual set of items by returning any true value from the random boolean list using a for loop
        return [self.universal[i] for i in range(self.n) if bool_list[i]]

    # display method
    def display_sets(self):
        #Display both sets and their boolean values
        #display set a
        set_a = self.get_set_from_boolean(self.bool_a)
        #display set b
        set_b = self.get_set_from_boolean(self.bool_b)

        print("=" * 50)
        #print universal set
        print("UNIVERSAL SET:")
        print(self.universal)
        #get boolean values
        print(f"\nSET A (Boolean): {self.bool_a}")
        #get element values
        print(f"SET A (Items): {set_a}")
        #same as set a
        print(f"\nSET B (Boolean): {self.bool_b}")
        print(f"SET B (Items): {set_b}")

        print("=" * 50)

    #operations
    def complement_a(self):
       #Return the complement of set A (everything in universal but not in A)
       #uses the function get_set_from_boolean to display output
       #creates set by checking which value is false in set A(bool_a) and adding it to bool_complement
        bool_complement = [not value for value in self.bool_a]
        return self.get_set_from_boolean(bool_complement)

    #union operation
    def union(self):
      #Returns the union A and B
      #uses the function get_set_from_boolean to display output
      #combines both sets into bool_union, then whichever values are true are displayed while false values are left undisplayed (maybe problem keeping false values in union set?)
        bool_union = [self.bool_a[i] or self.bool_b[i] for i in range(self.n)]
        return self.get_set_from_boolean(bool_union)

    # intersection operation
    def intersection(self):
       #Return the intersection of A and B
       #uses the function get_set_from_boolean to display output
       #creates set bool_intersection by checking if both values in current loop are true, if true then add to bool_intersection else leave out
        bool_intersection = [self.bool_a[i] and self.bool_b[i] for i in range(self.n)]
        return self.get_set_from_boolean(bool_intersection)

    # 4. Difference operation
    def difference_a_minus_b(self):
      #Return A - B
      # uses the function get_set_from_boolean to display output
      # creates set bool_difference by checking if set a value is true and checking if set b value is false
        bool_difference = [self.bool_a[i] and not self.bool_b[i] for i in range(self.n)]
        return self.get_set_from_boolean(bool_difference)

    # Symmetric difference
    def symmetric_difference(self):
        #Return symmetric difference (elements in A or B but not in both)
        # uses the function get_set_from_boolean to display output
        #creats bool_sym_set by using the XOR(^) operator to check that only 1 set has a true value and the other set has a false value which makes the element unique
        bool_sym_diff = [self.bool_a[i] ^ self.bool_b[i] for i in range(self.n)]  # XOR operator
        return self.get_set_from_boolean(bool_sym_diff)

# Example usage
if __name__ == "__main__":
    # Create an instance with random sets
    sets = Part1_OrdinarySets()

    # Display the original sets
    sets.display_sets()