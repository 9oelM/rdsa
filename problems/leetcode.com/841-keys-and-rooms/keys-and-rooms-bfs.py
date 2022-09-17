from queue import Queue
from typing import Dict, List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0:
          return True
        queue = Queue[int]()
        if len(rooms[0]) > 0: 
            for k in rooms[0]: 
              queue.put(k)
        visited: Dict[bool, int] = { 0: True }

        while not queue.empty() and len(visited) != len(rooms):
          key = queue.get()

          if key not in visited:
            visited[key] = True
            for k in rooms[key]:
              queue.put(k)
        return len(visited) == len(rooms)