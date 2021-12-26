# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    triLen = len(triangle)
    for rowIdx, row in reversed(list(enumerate(triangle))):
        for numIdx, num in enumerate(row):
            if rowIdx - 1 != -1 and numIdx + 1 != len(row): # not the topmost, not the rightmost
                bigger = max(row[numIdx], row[numIdx+1])
                triangle[rowIdx-1][numIdx] += bigger
    return triangle[0][0]
