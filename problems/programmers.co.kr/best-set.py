# https://programmers.co.kr/learn/courses/30/lessons/12938

from math import ceil

def solution(n: int, s: int) -> int:
    if n > s:
        return [-1]
    first = ceil(s / n)
    ans = [first for _ in range(n)]
    idx, total = 0, sum(ans)
    while total != s:
        total -= 1
        ans[idx] -= 1
        if idx + 1 == n: # last
            idx = 0
        else:
            idx += 1
    return ans

solution(3,9)
solution(4,14)
solution(4,15)
solution(4,17)
solution(16,17)