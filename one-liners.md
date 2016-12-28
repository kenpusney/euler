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
