from collections import defaultdict
from queue import Queue
from typing import Dict, List


class Solution:
    def toposort(self, n: int, directed_edges: Dict[int, List[int]]):
        adj: List[List[int]] = [[] for _ in range(n)]
        indegree: List[int] = [0] * n
        for edge in directed_edges:
            to, src = edge
            adj[src].append(to)
            indegree[to] += 1
        queue = Queue[int]()
        for i in range(n):
            if indegree[i] == 0:
                queue.put(i)
        while not queue.empty():
            curr: int = queue.get() 
            n -= 1
            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0: 
                    queue.put(v)
        return n == 0
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.toposort(numCourses, prerequisites)