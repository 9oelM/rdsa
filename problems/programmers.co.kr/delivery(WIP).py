# https://programmers.co.kr/learn/courses/30/lessons/12978

from typing import List


def solution(N: int, road: List[List[int]], k: int) -> int:
    graph = {}
    distanceMap = [[-1 for i in range(N + 1)] for j in range(N + 1)]

    for edge in road:
        if distanceMap[edge[0]][edge[1]] == -1:
            distanceMap[edge[0]][edge[1]] = edge[2]
        else:
            distanceMap[edge[0]][edge[1]] = min(distanceMap[edge[0]][edge[1]], edge[2])
        if distanceMap[edge[1]][edge[0]] == -1:
            distanceMap[edge[1]][edge[0]] = edge[2]
        else:
            distanceMap[edge[1]][edge[0]] = min(distanceMap[edge[1]][edge[0]], edge[2])

        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]

    visited = {}
    q = [(1, 0)]
    while q:
        nxt, nxtDist = q.pop(0)
        for node in graph[nxt]:
            if nxtDist + distanceMap[nxt][node] <= k:
                sumDist = nxtDist + distanceMap[nxt][node]
                if (node not in visited) or (node in visited and visited[
                    node] > sumDist):  # 2nd condition: if the node is already visited but the distance from node 1 is shorter
                    visited[node] = sumDist
                    q.append((node, sumDist))
    return len(visited)


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
