from queue import Queue
from typing import Dict, List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0:
          return True
        """
        There are n rooms labeled from 0 to n - 1 and 
        all the rooms are locked except for room 0. 
        Your goal is to visit all the rooms. 
        However, you cannot enter a locked room without having its key.

        When you visit a room, you may find a set of distinct keys in it. 
        Each key has a number on it, denoting which room it unlocks, and 
        you can take all of them with you to unlock the other rooms.

        Given an array rooms where rooms[i] is the set of keys that 
        you can obtain if you visited room i, return true 
        if you can visit all the rooms, or false otherwise.
        """

        queue = Queue[int]()
        if len(rooms[0]) > 0: 
            for k in rooms[0]: 
              queue.put(k)
        visited: Dict[bool, int] = {}

        while not queue.empty() and len(visited) != len(rooms):
          key = queue.get()

          if key not in visited:
            visited[key] = True
            for k in rooms[key]:
              queue.put(k)
        print(visited)
        return len(visited) == len(rooms)