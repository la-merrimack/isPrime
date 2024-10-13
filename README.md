# isPrime - v1.0.1
Version 1.0.1

## Overview
This repository contains an optimized version of the `isPrime()` function in the `findPrimes.py`

### Pre-Refactoring Analysis:
To accurately determine which part of the code required optimization, the following tools were used:

1. **cProfile**: 
   - A built-in Python profiler that was used to measure the execution time of different parts of the program.
   - Sorting by the `tottime` field in the cProfile output revealed that the `isPrime()` function was the primary bottleneck, making **over 3800 calls** and taking more than **105 seconds** to complete.
     <img width="884" alt="Screenshot 2024-10-13 at 1 25 29 PM" src="https://github.com/user-attachments/assets/5bd73165-20ab-4b0c-9e34-b7c638ec71bd">

   
2. **SnakeViz**:
   - A tool that visualizes profiling data from cProfile in the form of a web-based application. SnakeViz helped visualize the function calls data from cProfile and confirmed that the `isPrime()` function was causing the performance issues.
   
   ![Screenshot 2024-10-13 at 1 25 49 PM](https://github.com/user-attachments/assets/f7c76bac-871b-4d2d-abd0-c11ede516f00)

## Changes Made

The math.sqrt() method was used inaddtion to updates made to the `isPrime()` function to check the divisors up to the **square root of the number (sqrt(x))**. This reduced the time complexity from **O(x²)** to **O(√x)**, to help improve the performance of the code.

###  `isPrime()` update:
```python
import math

def isPrime(x):
    # if number is less than two they would not be prime numbers and return false
    if x< 2:
        return False

    # check for divsiors  of integer from 2 - sqrt(x)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i ==0: #if the remainder is 0, that means i is a divsor of x therefore is not a prime number
            return False
    return True

```

## Versioning:
- **Pre-optimization version**: `1.0.0`
- **Post-optimization version**: `1.0.1` (patch update to improve time complexity)
