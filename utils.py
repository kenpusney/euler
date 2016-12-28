import array
import itertools
import functools

def fib_i(a, b, i):
    if (i >= 0):
        return fib_i(b, a+b, i-1)
    return a

def fib(i): return fib_i(0, 1, i)

def primes(x):
    seive = array.array('b', [1] * x)
    for i in range(2, x):
        if seive[i]:
            for j in range(i*2, x, i):
                seive[j] = 0
    for i in range(2, x):
        if seive[i]:
            yield i

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return functools.reduce(lcm, args)

def slide(lst, size):
    if size > len(lst): return None
    index = 0
    while index + size <= len(lst):
        yield lst[index:index+size]
        index += 1