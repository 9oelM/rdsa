export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function deleteDuplicates(head: ListNode | null): ListNode | null {
  if (!head?.next) return head

  let prevUniqueNode: ListNode | null = null
  let foundDuplicate = false
  let newHead: ListNode | null = null

  while (head) {
    // if this happens, prev unique node does not have a unique value
    // in the sorted linked list anymore
    console.log(prevUniqueNode?.val)
    if (prevUniqueNode?.val === (head.next?.val ?? null)) {
      prevUniqueNode = null
    }
    // if two neighboring values are the same
    if (head.val === head.next?.val) {
      foundDuplicate = true
    // if two neighboring values are NOT the same and duplicates were found previosuly
    } else if (foundDuplicate) {
      // delete all duplicates nodes in between the previous unique node and the next node
      if (prevUniqueNode) {
        prevUniqueNode.next = head.next
      // could be the first unique node, so set the head and prevUniqueNode pointer to head.next
      } else {
        prevUniqueNode = head.next
        newHead = prevUniqueNode
      }
      foundDuplicate = false
    // if two neighboring values are not the same and there was no duplicate
    } else {
      prevUniqueNode = head
      if (!newHead) newHead = head
    }
    head = head.next
  }

  return newHead
};