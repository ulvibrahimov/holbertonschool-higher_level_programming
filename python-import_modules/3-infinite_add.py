#!/usr/bin/python3
import sys

def infinite_add():
    # Start the total at 0
    total = 0
    
    # Iterate through all command line arguments starting from index 1
    for arg in sys.argv[1:]:
        total += int(arg)
        
    print(total)

if __name__ == "__main__":
    infinite_add()
