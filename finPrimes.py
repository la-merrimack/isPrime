import random
import cProfile
import math

def guess():
    return random.randint(2, 5000)

def isPrime(x):
    # if number is less than two they would not be prime numbers and return false
    if x< 2:
        return False

    # check for divsiors  of integer from 2 - sqrt(x)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i ==0: #if the remainder is 0, that means i is a divsor of x therefore is not a prime number
            return False
    return True

def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes


cProfile.run('print(findPrimes(500)[:10])',sort='tottime')

# findPrimes(500)[:10]
