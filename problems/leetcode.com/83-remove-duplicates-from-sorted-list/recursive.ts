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
function deleteDuplicatesRecursively(ptr: ListNode | null): void {
  if (!ptr?.next) return
  if (ptr.val === ptr.next.val) {
    ptr.next = ptr.next.next
  } else {
    ptr = ptr.next
  }
  return deleteDuplicatesRecursively(ptr)
 }

function deleteDuplicates(head: ListNode | null): ListNode | null {
  deleteDuplicatesRecursively(head)
  return head
}
