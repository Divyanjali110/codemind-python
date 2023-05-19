import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def closest_prime_difference(num):
    if is_prime(num):
        return 0

    lower = num - 1
    upper = num + 1

    while True:
        if is_prime(lower):
            return num - lower
        elif is_prime(upper):
            return upper - num

        lower -= 1
        upper += 1

# Test the function
number = int(input())
difference = closest_prime_difference(number)
print(difference)
