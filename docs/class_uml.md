```mermaid

classDiagram
    class CLI_EntryPoint {
        <<Main Script>>
        string mode --part1|--part2
        main()
    }

    class Part1_OrdinarySets {
        list universal_set
        list bool_array_A
        list bool_array_B
        get_set_from_boolean(bool_set)
        generate_random_subset(uni_set)
        complement(bool_list)
        union(arr_A, arr_B)
        intersection(arr_A, arr_B)
        difference(arr_A, arr_B)
        symmetric_difference(arr_A, arr_B)
        display_sets()
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
