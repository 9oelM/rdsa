export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

/**
 * Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
 * Return the linked list sorted as well.
 */
function deleteDuplicates(head: ListNode | null): ListNode | null {
  const originalHead = head
  while (head && head.next) {
    if (head.val === head.next.val) {
      head.next = head.next.next
    } else {
      head = head.next
    }
  }

  return originalHead
}