def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both inputs are numeric (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False  # Return False if either input is not numeric
    
    # Check for division by zero to avoid runtime error
    if divisor == 0:
        return False  # Cannot divide by zero, so return False
    
    # Check if num is divisible by divisor
    # A number is divisible if the remainder when divided is 0
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

# Test scenario 1: Check if 10 is divisible by 2 (should return True)
print("Test 1: check_divisibility(10, 2)")
result1 = check_divisibility(10, 2)
print(f"Result: {result1}")
print()

# Test scenario 2: Check if 7 is divisible by 3 (should return False)
print("Test 2: check_divisibility(7, 3)")
result2 = check_divisibility(7, 3)
print(f"Result: {result2}")
print()
