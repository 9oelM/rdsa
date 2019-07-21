from typing import List

def solution(n : int, vertices : List[List[int]]) -> int:
    minDis = [0] * (n + 1)
    visited = [False] * (n + 1)
    graph = [[False for i in range(n + 1)] for j in range(n + 1)]

    # mark connections
    for vertex in vertices:
        graph[vertex[0]][vertex[1]] = True
        graph[vertex[1]][vertex[0]] = True

    for row in graph:
        print(row)
        
    queue = []
    for i in range(n+1):
        if graph[1][i]: # if connected with node 1
            queue.append((i, 1))
            visited[0] = True
            visited[i] = True
            minDis[i] = 1

    while queue:
        temp = queue[0]
        queue.pop()
        for i in range(n+1):
            if graph[temp[0]][i] and not visited[i]:
                visited[i] = True
                minDis[i] = 1 + temp[1]
                queue.append((i,minDis[i]))
    minDis = sorted(minDis, reverse=True)
    maximum = minDis[0]
    answer = 0
    
    for d in minDis:
        if d == maximum:
            answer += 1
        else:
            break
    
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
