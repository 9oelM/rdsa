from collections import defaultdict
from typing import Dict, List, Set

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
      graph = defaultdict(list)
      for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
      visited = set()
      return self.dfs(graph, visited, source, dest)

    def dfs(self, graph: Dict[int, List[int]], visited: Set[int], source: int, dest: int):
      if source == dest:
        return True
      visited.add(source)

      for neighbor in graph[source]:
        if not neighbor in visited:
          if self.dfs(graph, visited, neighbor, dest):
            return True
      return False
