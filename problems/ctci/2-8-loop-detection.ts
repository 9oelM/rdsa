// https://leetcode.com/problems/linked-list-cycle/

export class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }

function hasCycle(head: ListNode | null): boolean {
  let slow = head
  let fast = head

  while (true) {
    slow = slow?.next ?? null
    fast = fast?.next?.next ?? null
    if (slow !== fast || (slow !== null && fast !== null)) {
      break
    }
  }

  return slow === fast
};