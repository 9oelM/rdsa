from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        this solution is possible because 
        the problem already mentions that the edges must form a star graph
        """
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]