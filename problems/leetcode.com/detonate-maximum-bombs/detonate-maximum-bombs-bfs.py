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

    def bfs(self, node: int, visited: set[int], graph: DefaultDict[int, List[int]]):
        for child in graph[node]: # O(V)
            if child not in visited: # O(len(visited)) <= O(V)
              pass
              
                # graph[]
                # self.dfs(child, visited, graph) # if the child is not visited yet, visit it

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
            visited: set[int] = set([i])
            self.dfs(i, visited, graph)
            # update the length of visited vertices
            maximum_detonations = max(maximum_detonations, len(visited)) # O(V)

            # if it is at maximum in the middle of the search, just return it because it is the greatest possible number anyway
            if maximum_detonations == len(graph): return maximum_detonations

        return maximum_detonations

# bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
cases = [
    [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
]

s = Solution()
# for c in cases:
#     print(c)
#     print(s.maximumDetonation(c))