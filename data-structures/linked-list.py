class Node:
  nxt = None
  def __init__(self, data):
    self.data = data
  def __str__(self) -> str:
    nxt_notation = 'Node' if self.nxt is not None else 'None'
    return f'Node {{ data: {self.data}, nxt: {nxt_notation} }}'

"""
Singly linked list.
"""
class LinkedList:
  length = 0
  head = None
  tail = None

  def __init__(self, *args):
    self.length = len(args)

    current_node = None
    for _, data in enumerate(args):
      node = Node(data)
      if self.head is None:
        self.head = node
        current_node = node
      else:
        current_node.nxt = node
        current_node = node
    self.tail = current_node

  def delete(self, index):
    """
    Takes O(n) because it needs searching and deleting.
    But the deletion itself just takes O(1) time
    """
    if index >= self.length or index < 0:
      raise ValueError(f'{index} out of range.')

    current_node = self.head
    previous_node = None
    target_index = 0
    while target_index != index:
      previous_node = current_node
      current_node = current_node.nxt
      target_index += 1

    if previous_node is not None:
      previous_node.nxt = current_node.nxt
      if current_node.nxt is None:
        self.tail = None
    else:
      self.head = self.head.nxt

    self.length -= 1
  def last(self):
    return self.tail
  def first(self):
    return self.head
  def len(self):
    return self.length
  def append(self, data):
    new_last_elem = Node(data)
    self.tail.nxt = new_last_elem
    self.tail = new_last_elem
    self.length += 1
  def insert(self, index, data):
    """
    takes O(n) because it needs to traverse through the list and insert
    the actual insertion takes O(1)
    """
    if index >= self.length or index < 0:
      raise ValueError(f'{index} out of range.')

    if index == self.length - 1:
      self.append(data)
      return

    new_node = Node(data)
    current_node = self.head
    previous_node = None
    target_index = 0
    while target_index != index:
      previous_node = current_node
      current_node = current_node.nxt
      target_index += 1

    if previous_node is not None:
      previous_node.nxt = new_node
      new_node.nxt = current_node
      if new_node.nxt is None:
        self.tail = new_node
    else:
      previous_head = self.head
      self.head = new_node
      new_node.nxt = previous_head
    self.length += 1
  def at(self, index):
    """
    takes O(n) because it needs to traverse through the linked list
    """
    if index <= 0 or index >= self.length:
      return
    current_node = self.head
    target_index = 0
    while target_index != index:
      current_node = current_node.nxt
      target_index += 1
    return current_node.data
  def __str__(self):
    current_node = self.head
    all_data = ""
    while current_node is not None:
      pointer_or_empty_space = "" if all_data == "" else "->"
      all_data += f'{pointer_or_empty_space}{current_node.data}'
      current_node = current_node.nxt
    return f'{all_data}'

print("l = LinkedList(1,2,3,4)")
l = LinkedList(1,2,3,4)
print(l.len())
print(l)
print("l.append(5)")
l.append(5)
print("print(l)")
print(l)
print("l.append(6)")
l.append(6)
print(l)
print(l.len())
print("l.insert(0, 222)")
l.insert(0, 222)
print(l)
print(l.len())
print("l.insert(3, 555)")
l.insert(3, 555)
print(l)
print(l.len())
print("l.insert(1, 333)")
l.insert(1, 333)
print(l)
print(l.len())
print("l.insert(l.len() - 1, 99999)")
l.insert(l.len() - 1, 99999)
print(l)
print(l.len())
print("print(l.at(1))")
print(l.at(1))
print("print(l.last())")
print(l.last())
print("print(l.first())")
print(l.first())
print("l.delete(0)")
l.delete(0)
print(l)
print(l.len())
print("l.delete(l.len() - 1)")
l.delete(l.len() - 1)
print(l)
print(l.len())
print("l.delete(3)")
l.delete(3)
print(l)
print(l.len())