# https://leetcode.com/problems/detonate-the-maximum-bombs/

from collections import defaultdict
from math import sqrt
from typing import DefaultDict, List

# V = number of vertices

class Solution:
    def is_another_bomb_within_range(self, bomb: List[int], another_bomb: List[int]) -> bool: # O(1)
        """
        returns true if another bomb is in the circular range of a bomb
        """
        assert len(another_bomb) == 3 and len(bomb) == 3
        x2, y2 = another_bomb[0], another_bomb[1]
        x1, y1, radius = bomb[0], bomb[1], bomb[2]

        return sqrt((x2 - x1)**2 + (y2 - y1)**2) <= radius


    def bfs(self, source_node: int, graph: DefaultDict[int, List[int]]) -> int:
        """
        Run a BFS once, starting from source_node
        return the count of all visited nodes
        """
        # nothing is connected
        if not graph:
            return 1
        visited = {}
        queue = [source_node]
        visited[source_node] = True
        visited_cnt = 1

        while queue:
            s = queue.pop(0)
            for i in graph[s]:
                if not i in visited:
                    queue.append(i)
                    visited[i] = True
                    visited_cnt += 1

        return visited_cnt

    def build_graph(self, bombs: List[List[int]]) -> DefaultDict[int, List[int]]:
        graph = defaultdict(list)
        for i, bomb0 in enumerate(bombs): # O(V)
            for j, bomb1 in enumerate(bombs): # O(V)
                if i == j: continue
                if self.is_another_bomb_within_range(bomb0, bomb1): # O(1)
                    # i and j are connected
                    graph[i].append(j) # O(1)
        return graph

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, maximum_detonations = len(bombs), 0

        graph = self.build_graph(bombs)

        for i in range(n): # O(V)
            maximum_detonations = max(self.bfs(i, graph), maximum_detonations)

        return maximum_detonations

# bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
cases = [
    [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]],
    [[1,1,5],[10,10,5]],
    [[1,1,100],[81,61,60]]
]

s = Solution()
for c in cases:
    print(s.maximumDetonation(c))