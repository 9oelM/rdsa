# https://programmers.co.kr/learn/courses/30/lessons/43104

def solution(N : int) -> int:
    if N <= 2:
        return [4,6][N-1]
    else:
        crnt = 4
        nxt = 6
        for _ in range(N-1):
            crnt, nxt = nxt, crnt+nxt
        return crnt
