
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import sqrt

def isPrime(number):
    for i in range(2,int(sqrt(number)+1)):
        if number%i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'{number_of_primes} is 0 or less which is not allowed!')
    list = []
    n = 2
    while len(list) < number_of_primes:
        if isPrime(n):
            list.append(n)
        n += 1
    return list

print(primes(0))
