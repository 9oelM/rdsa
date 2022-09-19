# Definition for a Node.
from queue import Queue
from typing import Dict, List, Tuple
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
      if not node:
        return None
      """
      straightforward. put discovered nodes in queue
      and copy its neighbors. BFS.
      """
      clones = { node.val: Node(node.val, []) }
      originals = Queue[Node]()

      originals.put(node)
      while not originals.empty():
        vertex_original = originals.get()
        vertex_clone = clones[vertex_original.val]

        for neighbor in vertex_original.neighbors:
          if neighbor.val not in clones:
            clones[neighbor.val] = Node(neighbor.val, [])
            originals.put(neighbor)
          vertex_clone.neighbors.append(clones[neighbor.val])
      return clones[node.val]