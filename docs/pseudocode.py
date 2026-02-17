```python

    class CLI_EntryPoint {
        string mode --part1|--part2
        main()
    }

    class Part1_OrdinarySets {

        list universal_set
        list bit_array_A
        list bit_array_B

        generate_random_subset()
          return list bit_array length of universal_set

        complement(arr_A)
          return not A for A, U

        union(arr_A, arr_B)
          return A or B for A, B

        intersection(arr_A, arr_B)
          return A and B for A, B

        difference(arr_A, arr_B)
          return A and not B for A, B

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
        additive_union(bag_A, bag_B)
        standard_union(bag_A, bag_B)
        intersection(bag_A, bag_B)
        difference(bag_A, bag_B)
        display_results(label, counter_obj)
    }

```
