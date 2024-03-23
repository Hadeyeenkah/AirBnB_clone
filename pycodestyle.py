#!/usr/bin/python3
"""Resemblance of a calculator with arguments passed by command"""
from sys import argv, stderr


def calculator(argv):
    """Calcuaator 
    result = 0
    if len(argv) != 4:
        print("Usage: number1 operator number2", file=stderr)
        return
    else:
        try:
            a = int(argv[1])
            b = int(argv[3])
        except ValueError:
            print("Please provide valid numbers", file=stderr)
            return
        if argv[2] == '+':
            result = a + b
            print(f"The sum of {a:d} and {b:d} is: {result:d}")
        elif argv[2] == '-':
            result = a - b
            print(f"The difference of {a} and {b} is: {result}")
        elif argv[2] == '*':
            result = a * b
            print(f"The product of {a} and {b} is: {result}")
        elif argv[2] == '/':
            try:
                result = a / b
                print(f"The division of {a} and {b} is: {result}")
            except ZeroDivisionError:
                print("Error: Dividing by 0", file=stderr)
        else:
            print("Unsupported operator(+, *, / and -)", file=stderr)


calculator(argv)
