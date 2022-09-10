import { linkedListTestCases, LinkedListNode } from './linkedlist';

/**
 * You are given an access to only the node that is to be deleted
 */
function removeMiddleNode<Data>(node: LinkedListNode<Data>) {
  if (node.next) {
    node.data = node.next.data 
    node.next = node.next.next

    return true
  } else {
    return false
  }
}

linkedListTestCases.forEach((c, i, array) => {
  const secondNode = c.head.next
  if (!secondNode) return
  removeMiddleNode(secondNode)
  c.printLinkedList()
  console.log(`---------`)
})