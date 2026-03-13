#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # This creates a completely independent copy of the list
    new_list = my_list[:]
    
    # If index is invalid, return the copy untouched
    if idx < 0 or idx >= len(my_list):
        return new_list
        
    # If index is valid, replace the element in the COPY
    new_list[idx] = element
    return new_list
