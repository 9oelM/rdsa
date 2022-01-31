from typing import List


class DoublyLinkedListNode:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X: List[DoublyLinkedListNode]) -> None:
        for a in X:
            self.insert_last(a)

    def get_at(self, i: int) -> None:
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x) -> None:
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x) -> None:
        ###########################
        # Part (a): Implement me! #
        ###########################
        pass

    def insert_last(self, x) -> None:
        ###########################
        # Part (a): Implement me! #
        ###########################
        pass

    def delete_first(self) -> None:
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        return x

    def delete_last(self) -> None:
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        return x

    def remove(self, x1, x2) -> None:
        L2 = DoublyLinkedList()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        return L2

    def splice(self, x, L2) -> None:
        ###########################
        # Part (c): Implement me! # 
        ###########################
        pass
