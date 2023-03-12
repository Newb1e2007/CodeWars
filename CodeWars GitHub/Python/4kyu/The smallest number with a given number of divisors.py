from math import isqrt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def g(n,i):
    p=primes[i]
    m=p**(n-1)
    for d in range(2,isqrt(n)+1):
        if n%d==0: m=min(m,p**(d-1)*g(n//d,i+1),p**(n//d-1)*g(d,i+1))
    return m

def f(n):return g(n,0)


# -------------------------------------------------------------------

from gmpy2 import next_prime
from math import prod
from itertools import combinations

def primes(n):
    res = [2]
    while len(res) < n:
        res.append(next_prime(res[-1]))
    return res

PRIMES = primes(14)

def factor(n):
    res, d = [], 2
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res

def f(d: int) -> int:
    ps = factor(d)
    n = len(ps)
    res = []
    for k in range(n):
        for cs in combinations(range(1, n), k):
            xs = sorted((prod(ps[i:j]) for i, j in zip((0,) + cs, cs + (n,))), reverse=True)
            res.append(prod(p ** (e - 1) for p, e in zip(PRIMES, xs)))
    return min(res, default=1)