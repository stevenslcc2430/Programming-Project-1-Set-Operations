import argparse
from collections import Counter

# Setup the CLI argparser 
parser = argparse.ArgumentParser(description="Set vs Multiset Project")
parser.add_argument("--select", choices=["set", "bag"], required=True, help="Choose 'set' for Bit Strings or 'bag' for Multisets")

args = parser.parse_args()

# Select Logic
if args.mode == "set":
    print("Running Part 1: Ordinary Sets - Bit strings")
    sets = Part1_OrdinarySets()
    # Display the original sets
    sets.display_sets()
    
elif args.mode == "bag":
    print("Running Part 2: Multisets")
    multisets = Part2_Multisets()
    # Display multiset operations
    multisets.display_bags()
