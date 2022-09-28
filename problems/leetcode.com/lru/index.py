from typing import Dict


class LinkedListNode:
    def __init__(self, key: int, value: int):
        self.prev = None
        self.nxt = None
        self.key = key
        self.value = value

class LRUCache:    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, LinkedListNode] = {}
        self.head = LinkedListNode(0, 0)
        self.tail = LinkedListNode(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        return the value if the key exists
        
        if the key exists in the hash table:
        update the linkedlist, so that:
        - the element in the linkedlist that was pointed to by this key is now removed
        - the head is now the element that was just accessed
        """
        if key in self.cache:
            removed_node = self.cache[key]
            self.remove_node(removed_node)
            self.insert_after_tail(removed_node)
            return removed_node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        """
        if the key exists in the hash table:
        update the linked list, so that:
        - the element in the linkedlist that was pointed to by this key is now removed
        - the head is now the element that was just put
        
        if the key does not exist in the hash table:
        - add the key and value pair to the hash table
        - the head is now the element that was just put
        - if the length of the hash table exceeds the capacity, remove the tail from the linkedlist
        """
        if key in self.cache:
            self.remove_node(self.cache[key])
        node = LinkedListNode(key, value)
        self.insert_after_tail(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            self.remove_node(self.head.nxt)
            del self.cache[self.head.nxt.key]
    
    def insert_after_tail(self, node: LinkedListNode) -> None:
        prev = self.tail.prev
        prev.nxt = node
        self.tail.prev = node
        node.prev = prev
        node.nxt = self.tail

    def remove_node(self, node: LinkedListNode) -> None:
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev
