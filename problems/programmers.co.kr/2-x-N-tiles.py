# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    crnt = 1
    nxt = 2
    if n <= 2:
        return [crnt, nxt][n-1]
    for _ in range(n-2):
        nxt, crnt = crnt+nxt, nxt
    return nxt % 1000000007

print(solution(3))

