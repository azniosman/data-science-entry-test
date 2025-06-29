def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the input is actually a dictionary
    if not isinstance(dct, dict):
        return dct  # Return original input if not a dictionary
    
    # Check if the key already exists in the dictionary
    if key in dct:
        # Print the original value before updating
        print(f"Original value for key '{key}': {dct[key]}")
    
    # Update the dictionary with the new key-value pair
    # This will either add a new key or update an existing one
    dct[key] = value
    
    # Return the updated dictionary
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Test scenario 1: Add a new key-value pair to an empty dictionary
print("Test 1: update_dictionary({}, 'name', 'Alice')")
result1 = update_dictionary({}, "name", "Alice")
print(f"Result: {result1}")
print()

# Test scenario 2: Update an existing key in a dictionary (should print original value)
print("Test 2: update_dictionary({'age': 25}, 'age', 26)")
result2 = update_dictionary({"age": 25}, "age", 26)
print(f"Result: {result2}")
print()
