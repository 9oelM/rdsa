# https://programmers.co.kr/learn/courses/30/lessons/42861
import sys

def solution(n, costs):
    costsArray = [[0 for _ in range(n)] for __ in range(n)]
    graph = [[] for _ in range(n)]
    for cost in costs:
        costsArray[cost[0]][cost[1]] = cost[2]
        costsArray[cost[1]][cost[0]] = cost[2]
        graph[cost[0]] += [cost[1]]
        graph[cost[1]] += [cost[0]]

    for idx, vertex in enumerate(graph):
        # 1. must be connected to all nodes in the graph
        # 2. must be the smallest cost

        # Try to start from all nodes
        visited = [False] * n
        queue = [idx]
        visited[idx] = True
        minCost = sys.maxsize

        while queue:
            nxt = queue.pop(0)
            for node in graph[nxt]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)
                    
    
    return costsArray, graph

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
