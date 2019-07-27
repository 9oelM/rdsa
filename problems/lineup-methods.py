from typing import Callable, Union, List


def fac(n: int) -> int:
    if n == 1:
        return 1
    return n * fac(n - 1)

def recur(combinations: int, n: int, k: int, ans: List[int], people: List[int]):
    eachPartLen = combinations / n
    for i in range(1, n + 1):
        if i * eachPartLen >= k:
            if i != 0: # if i == 0: k = k
                k = k - (i - 1) * eachPartLen
            if k == 0:  # last element
                k = eachPartLen
            # find ith number not yet used
            count = 0
            for idx in range(1, len(people)):
                if not people[idx]:
                    count += 1
                    if i == count:
                        people[idx] = True
                        ans.append(idx)
                        break
            break
    if combinations == 1:
        return ans
    else:
        return recur(combinations / n, n - 1, k, ans, people)

def solution(n: int, k: int) -> int:
    combinations = fac(n)
    eachPartLen = combinations / n
    people = [False for i in range(0, n+1)]  # leave idx 0 empty
    ans = []
    for i in range(1, n + 1):
        if i * eachPartLen >= k:
            if i != 0: # if i == 0: k = k
                k = k - (i - 1) * eachPartLen
            if k == 0:  # last element
                k = eachPartLen
            people[i] = True
            ans.append(i)
            break

    return recur(combinations / n, n - 1, k, ans, people)


solution(3, 5)

solution(4, 5)

solution(4, 19)