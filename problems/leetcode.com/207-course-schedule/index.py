from collections import defaultdict
from queue import Queue
from typing import Dict, List


class Solution:
    def toposort(self, n: int, directed_edges: Dict[int, List[int]]):
        adj: List[List[int]] = [[] for _ in range(n)]
        outdegree: List[int] = [0] * n
        for edge in directed_edges:
            src, to = edge
            adj[to].append(src)
            outdegree[src] += 1
        queue = Queue[int]()
        for i in range(n):
            if outdegree[i] == 0:
                queue.put(i)
        while not queue.empty():
            curr: int = queue.get() 
            n -= 1
            for v in adj[curr]:
                outdegree[v] -= 1
                if outdegree[v] == 0: 
                    queue.put(v)
        return n == 0
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.toposort(numCourses, prerequisites)