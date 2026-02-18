```python

    class CLI_EntryPoint {
        string mode --part1|--part2
        main()
    }

    class Part1_OrdinarySets {

        list universal_set
        list bool_array_A
        list bool_array_B

        generate_random_subset()
          return list bool_arr length of universal_set
        
        # Flips True to False and vice versa
        # NOT(A) - Complement
        complement(arr_A)
          return not A for A, U

        # A ∪ B - Union
        # True if in either A or B
        union(arr_A, arr_B)
          return A or B for A, B

        # A ∩ B - Intersection
        # True only if in both A and B
        intersection(arr_A, arr_B)
          return A and B for A, B

        # A - B - Difference
        # A and not B
        difference(arr_A, arr_B)
          return A and not B for A, B

        # A ⊕ B - Symmetric Difference
        # XOR, in exactly one of the sets, A != B
        symmetric_difference(arr_A, arr_B)
          return A != B for A, B

        display_results(label, result_bits)
          display labeled operation and universal set name-at-index list
    
    }

    class Part2_Multisets {
    
        Counter bag_A
        Counter bag_B
        list items
        
        generate_random_bag(items)
            force two random items into bag with multiplicity > 2
            fill the rest of bag with random items up to total count
            return bag

        # Adds the counts together    
        additive_union(bag_A, bag_B)
            return bag_a + bag_b

        # Takes the max count for each element
        standard_union(bag_A, bag_B)
            return bag_a | bag_b

        # Takes the min count for each element    
        intersection(bag_A, bag_B)
            return bag_a & bag_b

        # Subtracts counts of B from A, can't be negative
        difference(bag_A, bag_B)
            return bag_a - bag_b
            
        display_results(label, counter_obj)
    }

```
