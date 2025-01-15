#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. For example:
    5! = 5 * 4 * 3 * 2 * 1 = 120

    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
