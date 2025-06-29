def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if the input is actually a string
    if not isinstance(s, str):
        return s  # Return original input if not a string
    
    # Reverse the string using slicing with step -1
    # This creates a new string with characters in reverse order
    reversed_string = s[::-1]
    
    return reversed_string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Test scenario 1: Reverse the string "Hello World"
print("Test 1: string_reverse('Hello World')")
result1 = string_reverse("Hello World")
print(f"Result: '{result1}'")
print()

# Test scenario 2: Reverse the string "Python"
print("Test 2: string_reverse('Python')")
result2 = string_reverse("Python")
print(f"Result: '{result2}'")
print()
