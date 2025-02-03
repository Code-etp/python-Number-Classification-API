import math

def is_armstrong_number(number):
    """Check if a number is an Armstrong number."""
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect_number(number):
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, number) if number % i == 0) == number

def digit_sum(number):
    """Calculate the sum of digits in a number."""
    return sum(int(digit) for digit in str(number))
