# Definition for a Node.
from collections import defaultdict
from typing import Dict, List, Optional, Union


class Node:
    def __init__(self, x: int, nxt: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nxt
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
          return None
        linked_list_nodes: List[Node] = []
        while head:
          head_next = head.next
          head.next = Node(head.val)
          linked_list_nodes.append(head)
          head = head_next
        for i, original_node in enumerate(linked_list_nodes):
          if original_node.random:
            # equivalent to new_node.random = original_node.new_node
            original_node.next.random = original_node.random.next
          linked_list_nodes[i] = original_node.next
        prev_node: Union[Node, None] = None
        for node in linked_list_nodes:
          if prev_node:
            prev_node.next = node
          prev_node = node
        return linked_list_nodes[0]
          
        