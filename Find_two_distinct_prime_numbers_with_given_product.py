import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def find_distinct_primes(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            return i, num // i

    return -1, -1

# Test the function
number = int(input())
prime1, prime2 = find_distinct_primes(number)

if prime1 != -1:
    print(prime1, prime2)
else:
    print("-1")
