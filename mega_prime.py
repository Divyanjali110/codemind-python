import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def is_mega_prime(num):
    if not is_prime(num):
        return False

    while num > 0:
        digit = num % 10
        if not is_prime(digit):
            return False
        num //= 10

    return True

# Test the function
number = int(input())

if is_mega_prime(number):
    print("Mega Prime")
else:
    print("Not Mega Prime")
