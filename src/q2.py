def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if the input is actually a list
    if not isinstance(lst, list):
        return lst  # Return original input if not a list
    
    # Create a new list to store the modified values
    modified_list = []
    
    # Iterate through each element in the list
    for item in lst:
        # If the current item matches the value to find, replace it
        if item == find_val:
            modified_list.append(replace_val)
        else:
            # Otherwise, keep the original item
            modified_list.append(item)
    
    return modified_list


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# Test scenario 1: Replace all occurrences of 2 with 5 in a numeric list
print("Test 1: find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)")
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(f"Result: {result1}")
print()

# Test scenario 2: Replace all occurrences of "apple" with "orange" in a string list
print("Test 2: find_and_replace(['apple', 'banana', 'apple'], 'apple', 'orange')")
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(f"Result: {result2}")
print()
