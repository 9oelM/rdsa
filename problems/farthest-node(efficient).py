from typing import List

def solution(n : int, vertices : List[List[int]]) -> int:
    graph = [ [] for _ in range(n + 1)]
    distances = [ 0 for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = [0]
    visited[0] = True
    for a, b in vertices:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    while queue:
        i = queue.pop(0)
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1
    print(distances)
    distances.sort(reverse=True)
    answer = distances.count(distances[0])
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
