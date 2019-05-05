# https://programmers.co.kr/learn/courses/30/lessons/42839
from typing import List, Callable

intToList = Callable[[int], List[int]]

def memoize(func : intToList) -> intToList:
    print('with memoize')
    cache = []
    def memoizer(n):
        nonlocal cache
        if n > len(cache): # haven't met this n before
            cache = func(n) # if new, calculate from scratch again
        return cache 
    return memoizer


def getPrime(n : int) -> List[int]:
    prime = [True for i in range(n + 1)]
    fac = 2
    while fac * fac <= n + 1:
        if prime[fac]:
            for i in range(fac*fac, n + 1, fac):
                prime[i] = False
        fac += 1
    return prime

def isPrime(n : int) -> bool:
    return getPrime(n)[n]
    
def solution(numbers):
    import itertools
    ans = list(map(''.join, itertools.permutations(list(numbers))))
    print(ans)
    return 1
