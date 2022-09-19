from collections import defaultdict
from queue import Queue
from typing import Dict, List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        directed_graph: Dict[int, List[int]] = defaultdict(list)
        indegrees: Dict[int, int] = defaultdict(int)
        ordering: List[int] = []

        for edge in prerequisites:
          to, src = edge
          directed_graph[src].append(to)
          indegrees[to] += 1

        queue = Queue[int]()
        for vertex in range(numCourses):
          if indegrees[vertex] == 0:
            queue.put(vertex)

        while not queue.empty():
          vertex = queue.get()
          ordering.append(vertex)

          for neighbor in directed_graph[vertex]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
              queue.put(neighbor)
        if len(ordering) != numCourses:
          return []
        return ordering