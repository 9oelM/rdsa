from turtle import left
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, binary_tree: List[int], node: TreeNode) -> List[int]:
      binary_tree.append(node.val)

      if node.left:
        self.traverse(binary_tree, node.left)
      else:
        binary_tree.append(None)

      if node.right:
        self.traverse(binary_tree, node.right)
      else:
        binary_tree.append(None)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      binary_trees = []
      for _, root_node in enumerate([p, q]):
        current_node: Optional[TreeNode] = root_node
        binary_tree = []
        if not root_node:
          binary_trees.append(binary_tree)
          continue
        self.traverse(binary_tree, current_node)
        binary_trees.append(binary_tree)
      return binary_trees[0] == binary_trees[1] # O(len(binary_tree))

class Solution: 
    def isSameTree(self, p, q):
      if p and q:
          return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
      return p is q