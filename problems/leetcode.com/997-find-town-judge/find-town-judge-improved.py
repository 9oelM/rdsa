from typing import List


def findJudge(N, trust: List[List[int]]):
    count = [0] * (N + 1)
    for i, j in trust:
        # outdegree (i trusts j)
        count[i] -= 1
        # indegree (j is trusted by i)
        count[j] += 1
    for i in range(1, N + 1):
        if count[i] == N - 1:
            return i
    return -1