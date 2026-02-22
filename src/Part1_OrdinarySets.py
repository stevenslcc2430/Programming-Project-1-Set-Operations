import random

class Part1_OrdinarySets:
    def __init__(self):
        self.universal = ["Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Pasta", "Yogurt", "Tea", "Oatmeal"]
        self.n = len(self.universal)
         
        # Create random boolean lists for two subsets
        self.bool_a = [random.choice([True, False]) for _ in range(self.n)]
        self.bool_b = [random.choice([True, False]) for _ in range(self.n)]
        
        A = self.bool_a
        B = self.bool_b
        
        # Operations
        # Return the complement of set A (everything in universal but not in A)
        # Uses the function get_set_from_boolean to display output
        # Creates set by checking which value is false in set A(bool_a) and adding it to bool_complement
        self.complement_a = [not value for value in A]

        # Union Operation
        # Returns the union A and B
        # Uses the function get_set_from_boolean to display output
        # Combines both sets into bool_union, then whichever values are true are displayed while false values are left undisplayed (maybe problem keeping false values in union set?)
        self.union = [A[i] or B[i] for i in range(self.n)]

        # Intersection operation
        # Return the intersection of A and B
        # Uses the function get_set_from_boolean to display output
        # Creates set bool_intersection by checking if both values in current loop are true, if true then add to bool_intersection else leave out
        self.intersection = [A[i] and B[i] for i in range(self.n)]

        # Difference operation
        # Return A - B
        # uses the function get_set_from_boolean to display output
        # creates set bool_difference by checking if set a value is true and checking if set b value is false
        self.difference_a_minus_b = [A[i] and not B[i] for i in range(self.n)]

        # Symmetric difference
        # Return symmetric difference (elements in A or B but not in both)
        # uses the function get_set_from_boolean to display output
        # creats bool_sym_set by using the XOR(^) operator to check that only 1 set has a true value and the other set has a false value which makes the element unique
        self.symmetric_difference = [A[i] ^ B[i] for i in range(self.n)]  # XOR operator

    def get_set_from_boolean(self, bool_list):
        #Convert boolean values to actual set of items by returning any true value from the random boolean list using a for loop
        return [self.universal[i] for i in range(self.n) if bool_list[i]]




    # Display method

    def display_sets(self):
        #
        print(f"{'Operation':<25} | {'Bit Representation':<25} | {'Actual Items'}")
        print("-" * 100)
        print(f"{'Subset A':<25} | {list(map(int, self.bool_a))} | {self.get_set_from_boolean(self.bool_a)}")
        print(f"{'Subset B':<25} | {list(map(int, self.bool_b))} | {self.get_set_from_boolean(self.bool_b)}")
        print(f"{'NOT(A) - Complement':<25} | {list(map(int, self.complement_a))} | {self.get_set_from_boolean(self.complement_a)}")
        print(f"{'A ∪ B - Union':<25} | {list(map(int, self.union))} | {self.get_set_from_boolean(self.union)}")
        print(f"{'A ∩ B - Intersection':<25} | {list(map(int, self.intersection))} | {self.get_set_from_boolean(self.intersection)}")
        print(f"{'A - B - Difference':<25} | {list(map(int, self.difference_a_minus_b))} | {self.get_set_from_boolean(self.difference_a_minus_b)}")
        print(f"{'A ⊕ B - Symm Diff':<25} | {list(map(int, self.symmetric_difference))} | {self.get_set_from_boolean(self.symmetric_difference)}")
        
# Example usage
if __name__ == "__main__":
    # Create an instance with random sets
    sets = Part1_OrdinarySets()

    # Display the original sets
    sets.display_sets()
