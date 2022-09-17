from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        There is an undirected star graph consisting of n nodes labeled from 1 to n. 
        A star graph is a graph where there is one center node and exactly n - 1 edges
        that connect the center node with every other node.

        You are given a 2D integer array edges where each edges[i] = [ui, vi]
        indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
        """
        graph = [0] * (len(edges) + 2)
        for e in edges:
          graph[e[0]], graph[e[1]] = graph[e[0]] + 1, graph[e[1]] + 1
        return graph.index(len(edges))