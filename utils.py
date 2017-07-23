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

def divide(n):
    for i in range(1, n):
        yield (i, n - i)

def matrix(iterable, n):
    return map(lambda gp: list(map(lambda it: it[1], gp[1])), 
            itertools.groupby(enumerate(iterable), lambda it: it[0] // n))

def rows(matrix, size):
    lst = list(matrix)
    for i in range(size):
        yield lst[i]

def cols(matrix, size):
    for i in range(size):
        yield [r[i] for r in matrix]

def ldiags(m, size):
    for i in range(size):
        yield lcollect(m, 0, i, size)
    for i in range(1, size):
        yield lcollect(m, i, 1, size)

def lcollect(m, i, j, size):
    for x in range(i, size):
        yield m[x][j]
        j += 1
        if j >= size:
            break

def rdiags(m, size):
    for i in range(size):
        yield rcollect(m, 0, i, size)
    for i in range(1, size):
        yield rcollect(m, i, size-1, size)

def rcollect(m, i, j, size):
    for x in range(i, size):
        yield m[x][j]
        j -= 1
        if j < 0:
            break

def factors(n):
    from functools import reduce
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
