```mermaid

classDiagram
    class CLI_EntryPoint {
        <<Main Script>>
        string mode --part1|--part2
        main()
    }

    class Part1_OrdinarySets {
        list universal_set
        list bit_array_A
        list bit_array_B
        generate_random_sets()
        complement(bit_array)
        union(arr_A, arr_B)
        intersection(arr_A, arr_B)
        difference(arr_A, arr_B)
        symmetric_difference(arr_A, arr_B)
        display_results(label, result_bits)
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

    CLI_EntryPoint --> Part1_OrdinarySets : if args.part1
    CLI_EntryPoint --> Part2_Multisets : if args.part2
