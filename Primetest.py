import math

def prime_check(n):
    prime = (n**2 + n + 41)
    return prime

def isprime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False

for i in range(100):
    x = prime_check(i)
    if not isprime(x):
        print(f'{x} is Not a prime')
    else:
         print(x)