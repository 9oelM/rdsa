from typing import Dict, List

class Solution:
    def dfs(self, rooms: List[List[int]], visited: Dict[bool, int], src: int):
      for key in rooms[src]:
        if key not in visited:
          visited[key] = True
          self.dfs(rooms, visited, key)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0:
          return True
        visited: Dict[int, int] = { 0: True }
        self.dfs(rooms, visited, 0)
        return len(visited) == len(rooms)