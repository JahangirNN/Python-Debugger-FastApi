from fastapi import APIRouter, HTTPException, Body
import random


router = APIRouter()

temp_code = [
    {
        "id": 0,
        "name": "Add Two Numbers",
        "tags": [],
        "code": "def add_numbers(a, b):\nreturn a + b\n\nprint(add_numbers(2, 3))",
        "hint": "The code defines a Python function named add_numbers that takes two arguments (a and b) and returns their sum. Fix the indentation of the return statement.",
        "test_cases": [
            { "input": "add_numbers(2, 3)", "expected": 5 },
            { "input": "add_numbers(-1, 4)", "expected": 3 },
            { "input": "add_numbers(0, 0)", "expected": 0 },
        ]
    },
    {
        "id": 1,
        "name": "Find the Largest Number",
        "tags": [],
        "code": "def find_max(numbers):\n    max_num = numbers[0]\n    for num in numbers:\n    if num > max_num:\n        max_num = num\n    return max_num\n\nprint(find_max([1, 2, 3, 4, 5]))",
        "hint": "The code attempts to find the maximum value in a list. Check the indentation inside the for loop.",
        "test_cases": [
            { "input": "find_max([1, 2, 3, 4, 5])", "expected": 5 },
            { "input": "find_max([-1, -5, -3])", "expected": -1 },
            { "input": "find_max([0])", "expected": 0 },
        ]
    },
    {
        "id": 2,
        "name": "Check Even or Odd",
        "tags": [],
        "code": "def check_even_odd(n):\n    if n % 2 = 0:\n        return 'Even'\n    else:\n        return 'Odd'\n\nprint(check_even_odd(4))",
        "hint": "The code determines if a number is even or odd. Check the equality operator in the if condition.",
        "test_cases": [
            { "input": "check_even_odd(4)", "expected": "Even" },
            { "input": "check_even_odd(7)", "expected": "Odd" },
            { "input": "check_even_odd(0)", "expected": "Even" },
        ]
    },
    {
        "id": 3,
        "name": "Reverse a String",
        "tags": [],
        "code": "def reverse_string(s):\n    return ''.join(reversed[s])\n\nprint(reverse_string('hello'))",
        "hint": "The code is meant to reverse a string. Check the syntax for calling the reversed function.",
        "test_cases": [
            { "input": "reverse_string('hello')", "expected": "olleh" },
            { "input": "reverse_string('world')", "expected": "dlrow" },
            { "input": "reverse_string('')", "expected": "" },
        ]
    },
    {
        "id": 4,
        "name": "Calculate Factorial",
        "tags": [],
        "code": "def factorial(n):\n    if n == 1:\n    return 1\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5))",
        "hint": "The code calculates the factorial of a number using recursion. Check the indentation of the return statement in the if condition.",
        "test_cases": [
            { "input": "factorial(5)", "expected": 120 },
            { "input": "factorial(1)", "expected": 1 },
            { "input": "factorial(3)", "expected": 6 },
        ]
    },
    {
        "id": 5,
        "name": "Count Vowels in a String",
        "tags": [],
        "code": "def count_vowels(s):\n    count = 0\n    for char in s:\n    if char in 'aeiouAEIOU':\n    count += 1\n    return count\n\nprint(count_vowels('hello world'))",
        "hint": "The code is meant to count the number of vowels in a string. Check the indentation inside the for loop.",
        "test_cases": [
            { "input": "count_vowels('hello world')", "expected": 3 },
            { "input": "count_vowels('AEIOU')", "expected": 5 },
            { "input": "count_vowels('bcdfghjkl')", "expected": 0 },
        ]
    },
    {
        "id": 6,
        "name": "Calculate Power of a Number",
        "tags": [],
        "code": "def power(x, n):\n    if n == 0:\n    return 1\n    else:\n    return x * power(x, n - 1)\n\nprint(power(2, 3))",
        "hint": "The code calculates the power of a number using recursion. Check the indentation of the return statement in the if condition.",
        "test_cases": [
            { "input": "power(2, 3)", "expected": 8 },
            { "input": "power(5, 0)", "expected": 1 },
            { "input": "power(3, 2)", "expected": 9 },
        ]
    },
    {
        "id": 7,
        "name": "Check Prime Number",
        "tags": [],
        "code": "def is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, n):\n    if n % i == 0:\n    return False\n    return True\n\nprint(is_prime(7))",
        "hint": "The code checks if a number is prime. Check the indentation inside the for loop.",
        "test_cases": [
            { "input": "is_prime(7)", "expected": True },
            { "input": "is_prime(4)", "expected": False },
            { "input": "is_prime(1)", "expected": False },
        ]
    },
    {
        "id": 8,
        "name": "Generate Fibonacci Sequence",
        "tags": [],
        "code": "def fibonacci(n):\n    sequence = [0, 1]\n    for i in range(2, n):\n    next_value = sequence[i-1] + sequence[i-2]\n    sequence.append(next_value)\n    return sequence\n\nprint(fibonacci(5))",
        "hint": "The code generates a Fibonacci sequence. Check the indentation inside the for loop.",
        "test_cases": [
            { "input": "fibonacci(5)", "expected": [0, 1, 1, 2, 3] },
            { "input": "fibonacci(3)", "expected": [0, 1, 1] },
            { "input": "fibonacci(1)", "expected": [0] },
        ]
    },
    {
        "id": 9,
        "name": "Calculate Sum of a List",
        "tags": [],
        "code": "def sum_list(numbers):\n    total = 0\n    for num in numbers:\n    total += num\n    return total\n\nprint(sum_list([1, 2, 3, 4, 5]))",
        "hint": "The code calculates the sum of all numbers in a list. Check the indentation inside the for loop.",
        "test_cases": [
            { "input": "sum_list([1, 2, 3, 4, 5])", "expected": 15 },
            { "input": "sum_list([-1, 1, 0])", "expected": 0 },
            { "input": "sum_list([10])", "expected": 10 },
        ]
    }

]


@router.get("/get_code")
def get_code(id: int):
    try:
        for code in temp_code:
            if code["id"] == id:
                return code
            else:
                return code[random.randint(1, 4)]
        raise HTTPException(status_code=404, detail=f"Code with ID {id} not found")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID format")



