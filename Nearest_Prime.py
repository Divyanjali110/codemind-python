import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def find_nearest_prime(num):
    if is_prime(num):
        return num

    lower = num - 1
    upper = num + 1

    while True:
        if is_prime(lower):
            return lower
        elif is_prime(upper):
            return upper

        lower -= 1
        upper += 1

# Number of test cases
t = int(input())

for _ in range(t):
    number = int(input())
    nearest_prime = find_nearest_prime(number)
    print(nearest_prime)
