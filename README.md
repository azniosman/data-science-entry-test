# Data Science Entry Test - Solutions

This repository contains my solutions to the 7 Python coding problems for the NTU SCTP Advanced Professional Certificate in Data Science and AI technical assessment.

## Solutions Overview

### Question 1: Variable Swapping (`src/q1.py`)
**Problem**: Create a function that swaps two numeric variables using only those variables.
- ✅ Handles non-numeric inputs by returning -1
- ✅ Swaps numeric values using arithmetic operations
- ✅ Prints swapped values and returns tuple

**Test Results**:
- `swap("Apple", 10)` → Returns -1
- `swap(9, 17)` → Prints "x = 17, y = 9", Returns (17, 9)

### Question 2: Find and Replace (`src/q2.py`)
**Problem**: Search and replace all occurrences of a value in a list.
- ✅ Validates input is a list
- ✅ Replaces all matching values
- ✅ Returns modified list

**Test Results**:
- `find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)` → `[1, 5, 3, 4, 5, 5]`
- `find_and_replace(["apple", "banana", "apple"], "apple", "orange")` → `["orange", "banana", "orange"]`

### Question 3: Dictionary Update (`src/q3.py`)
**Problem**: Update dictionary with key-value pair, printing original value if key exists.
- ✅ Validates input is a dictionary
- ✅ Prints original value before updating existing keys
- ✅ Returns updated dictionary

**Test Results**:
- `update_dictionary({}, "name", "Alice")` → `{"name": "Alice"}`
- `update_dictionary({"age": 25}, "age", 26)` → Prints "Original value for key 'age': 25", Returns `{"age": 26}`

### Question 4: String Reversal (`src/q4.py`)
**Problem**: Reverse a given string.
- ✅ Validates input is a string
- ✅ Uses Python slicing for efficient reversal
- ✅ Returns reversed string

**Test Results**:
- `string_reverse("Hello World")` → `"dlroW olleH"`
- `string_reverse("Python")` → `"nohtyP"`

### Question 5: Divisibility Check (`src/q5.py`)
**Problem**: Check if one number is divisible by another.
- ✅ Validates both inputs are numeric
- ✅ Handles division by zero
- ✅ Returns boolean result

**Test Results**:
- `check_divisibility(10, 2)` → `True`
- `check_divisibility(7, 3)` → `False`

### Question 6: Find First Negative (`src/q6.py`)
**Problem**: Find first negative number in a list using while loop.
- ✅ Validates input is a list
- ✅ Uses while loop as required
- ✅ Returns first negative or "No negatives"

**Test Results**:
- `find_first_negative([3, 5, -1, 7, -2, 8])` → `-1`
- `find_first_negative([2, 10, 7, 0])` → `"No negatives"`

### Question 7: Car Class (`src/q7.py`)
**Problem**: Define a Car class with make, model, year attributes and describe_car method.
- ✅ Proper `__init__` method with all required attributes
- ✅ `describe_car()` method prints in "Year Make Model" format
- ✅ Well-documented with docstrings

**Test Results**:
- `Car("Toyota", "Corolla", 2020).describe_car()` → Prints `"2020 Toyota Corolla"`

## Code Quality Features

### ✅ Input Validation
All functions include proper input validation to handle edge cases and invalid data types.

### ✅ Comprehensive Comments
Each solution includes detailed comments explaining the logic and approach.

### ✅ Error Handling
Proper error handling for division by zero, type mismatches, and edge cases.

### ✅ Test Coverage
All required test scenarios are implemented and verified.

### ✅ Documentation
Clear docstrings and inline comments explain functionality.

## Running the Solutions

Each solution can be run independently:

```bash
# Run individual questions
python3 src/q1.py
python3 src/q2.py
python3 src/q3.py
python3 src/q4.py
python3 src/q5.py
python3 src/q6.py
python3 src/q7.py
```

## Test Logs

Test output logs are available in the `logs/` directory:
- `logs/q1_output.log` - q1.py test results
- `logs/q2_output.log` - q2.py test results  
- `logs/q3_output.log` - q3.py test results
- `logs/q4_output.log` - q4.py test results
- `logs/q5_output.log` - q5.py test results
- `logs/q6_output.log` - q6.py test results
- `logs/q7_output.log` - q7.py test results

## Repository Structure

```
├── README.md           # This file with solutions overview
├── src/               # Source code directory
│   ├── q1.py         # Variable swapping solution
│   ├── q2.py         # Find and replace solution
│   ├── q3.py         # Dictionary update solution
│   ├── q4.py         # String reversal solution
│   ├── q5.py         # Divisibility check solution
│   ├── q6.py         # Find first negative solution
│   └── q7.py         # Car class solution
├── logs/              # Test output logs
└── assets/            # Original screenshot assets
```

---

**Author**: Azni Osman  
**Assessment**: NTU SCTP Advanced Professional Certificate in Data Science and AI  
**Completion Time**: Under 2 hours as required  
**All Solutions**: ✅ Tested and Verified