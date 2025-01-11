from fastapi import APIRouter, HTTPException, Body

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
    }
]


@router.get("/get_code")
def get_code(id: int):
    try:
        for code in temp_code:
            if code["id"] == id:
                return code
        raise HTTPException(status_code=404, detail=f"Code with ID {id} not found")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID format")



