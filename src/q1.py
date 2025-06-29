def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values using arithmetic operations (only using x and y as variables)
    x = x + y  # x now contains the sum of original x and y
    y = x - y  # y now contains the original x value
    x = x - y  # x now contains the original y value
    
    # Print the swapped values as required
    print(f"x = {x}, y = {y}")
    
    # Return the swapped values
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Test scenario 1: "Apple", 10 (should return -1 since "Apple" is not numeric)
print("Test 1: swap('Apple', 10)")
result1 = swap("Apple", 10)
print(f"Result: {result1}")
print()

# Test scenario 2: 9, 17 (should swap the values and print them)
print("Test 2: swap(9, 17)")
result2 = swap(9, 17)
print(f"Result: {result2}")
print()
