from typing import List


class Solution:
  """
  Given a directed acyclic graph, 
  with n vertices numbered from 0 to n-1, and 
  an array edges where edges[i] = [fromi, toi] 
  represents a directed edge from node fromi to node toi.

  Find the smallest set of vertices from 
  which all nodes in the graph are reachable. 
  It's guaranteed that a unique solution exists.

  Notice that you can return the vertices in any order.
  """
  def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    # def dfs(src: int, path: List[int]):
    #   if src == n - 1 and len(ans) > len(path):
    #     ans = path
    #   elif src != n - 1:
    #     for v in edges[src]:
    #       dfs(v, path + [v])
    # ans: List[int] = []
    # dfs(0, )
    # return ans