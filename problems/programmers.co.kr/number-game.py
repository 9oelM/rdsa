
from typing import List

def solution(A: List[int], B: List[int]) -> int:
    A.sort()
    B.sort()
    score = 0
    i = 0
    for j in range(len(B)):
        if A[i] < B[j]:
            i += 1
            score += 1
    return score

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([1,2,3,4,5,6,7], [2,3,4,5,6,7,8]))
print(solution([1,2,2,2,5], [1,1,2,3,3]))
print(solution([2,2,2,2], [1,1,1,1]))