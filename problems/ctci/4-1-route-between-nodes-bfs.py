from collections import defaultdict
from queue import Queue
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
      graph = defaultdict(list)

      for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
      
      visited = defaultdict(bool)
      queue = Queue()
      queue.put(source)
      visited[source] = True
      while not queue.empty():
        vertex: int = queue.get()
        if vertex == destination:
          return True
        for v in graph[vertex]:
          if not visited[v]:
            visited[v] = True
            queue.put(v)
      
      return False