def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Check if the input is actually a list
    if not isinstance(lst, list):
        return "No negatives"  # Return default message if not a list
    
    # Initialize variables for the while loop
    index = 0  # Start at the first element
    
    # Use a while loop to iterate through the list
    while index < len(lst):
        # Check if the current element is a number and is negative
        if isinstance(lst[index], (int, float)) and lst[index] < 0:
            return lst[index]  # Return the first negative number found
        
        # Move to the next element
        index += 1
    
    # If we've gone through the entire list without finding a negative number
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

# Test scenario 1: List with negative numbers (should return -1, the first negative)
print("Test 1: find_first_negative([3, 5, -1, 7, -2, 8])")
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(f"Result: {result1}")
print()

# Test scenario 2: List with no negative numbers (should return "No negatives")
print("Test 2: find_first_negative([2, 10, 7, 0])")
result2 = find_first_negative([2, 10, 7, 0])
print(f"Result: {result2}")
print()
