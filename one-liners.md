One-liners for Euler
=======

## Setup

what you should do is to import following modules:
```python
import math
import itertools
from utils import *
```


### Problem 1

Python
```python
sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
```

### Problem 2

Python
```python
sum(filter(lambda x: x%2==0, [fib(i) for i in range(33)]))
```

### Problem 3

Python
```python
max([i for i in primes(int(math.sqrt(600851475143))) if 600851475143 % i ==0 ])
```

### Problem 4

Python
```python
max([int(m) for m in
     [str(x) for x in
        set([v[0] * v[1] for v in
            itertools.combinations_with_replacement(range(100, 999), 2)])]
     if m[0] == m[-1] and ''.join(reversed(m)) == m])
```

### Problem 5

Python
```python
functools.reduce(lcm, range(1, 21))
```

### Problem 6

Python
```python
sum(range(1, 101)) ** 2 - sum([i ** 2 for i in range(1, 101)])
```

### Problem 7

Python
```python
list(primes(200000))[10000]
```

### Problem 8

Python
```python
src = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''.replace("\n", "")
max([functools.reduce(lambda x, y: x * y, s) for s in slide(list(map(int, src)), 13)])
```

### Problem 9

Python
```python
def triplet(n):
    cache = set()
    for (i, j) in divide(n):
        for (j, k) in divide(j):
            fst, snd, trd = sorted([i, j, k])
            key = '-'.join(map(str, [fst, snd, trd]))
            if key in cache:
                continue
            if (fst ** 2 + snd ** 2 == trd ** 2):
                yield (fst, snd, trd)
            cache.update([key])
list(map(lambda t: functools.reduce(lambda a, b: a*b, t), triplet(1000)))
```

### Problem 10

Python
```python
sum(primes(2000000))
```

### Problem 13

```python
str(sum(map(int, text.split('\n'))))[0:10]
```

### Problem 16

```python
sum(map(int, list(str(2**1000))))
```

### Problem 20

```python
sum(map(int, list(str(fact(100)))))
```

### Problem 48

```python
solution48 = 0;
for i in range(1, 1001):
	solution48 += pow(i, i)

str(solution48)[-10:]
```
