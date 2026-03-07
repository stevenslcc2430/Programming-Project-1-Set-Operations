"""
Team #5

Team Members
- Steven Benjamin
- Alex Gonzalez
- Carlos Recinos

CS-2430-502
Project 1: Set Operations
"""

import argparse
from Part1_OrdinarySets import Part1_OrdinarySets
from Part2_Multisets import Part2_Multisets

# Setup the CLI argparser 
parser = argparse.ArgumentParser(description="Set vs Multiset Project")
parser.add_argument("--select", choices=["set", "bag"], required=True, help="Choose 'set' for Bit Strings or 'bag' for Multisets")

args = parser.parse_args()

# Select Logic
if args.select == "set":
    print("Running Part 1: Ordinary Sets - Bit strings")
    sets = Part1_OrdinarySets()
    # Display the original sets
    sets.display_sets()
    
elif args.select == "bag":
    print("Running Part 2: Multisets")
    multisets = Part2_Multisets()
    # Display multiset operations
    multisets.display_bags()
