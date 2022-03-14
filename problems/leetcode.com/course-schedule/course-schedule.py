from collections import defaultdict
from typing import DefaultDict, Dict, List

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

Graph = List[List[int]]

BEING_VISITED = -1
VISITED = 1
NOT_VISITED = 0

class Solution:
  """
  This problem is about nothing but a cycle detection.

  All courses can be taken under these conditions:
  1. The graph is a directed graph
  2. If there is a cycle, that means contradiction between prerequisites. So not all courses can be taken.
  3. All nodes don't necessarily have to be connected as long as they are without a cycle 
  """
  def dfs(self, node: int, graph: Graph, visited: List[List[int]]) -> bool:
    if visited[node] == BEING_VISITED: # Cycle
      return False
    if visited[node] == VISITED: # Already was visited
      return True

    visited[node] = BEING_VISITED

    for n in graph[node]:
      # visit children of a node, and if cyclic, return False
      is_acyclic = self.dfs(n, graph, visited)
      if not is_acyclic:
        return False

    visited[node] = VISITED
    return True

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for i in range(numCourses)]
    visited = [NOT_VISITED for i in range(numCourses)]
    for pair in prerequisites:
      course, prerequisite = pair
      graph[course].append(prerequisite)
    for i in range(numCourses):
      is_acyclic = self.dfs(i, graph, visited)
      if not is_acyclic:
        return False

    return True

s = Solution()
print(s.canFinish(2, [[1,0]]))
print(s.canFinish(2, [[1,0], [0, 1]]))