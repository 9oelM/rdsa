// https://leetcode.com/problems/linked-list-cycle/

export class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }

/**
 * ## Complexity
 * - time: 2n =
 * 
 * ## Workflow
 * Suppose your friend and you are running on the same, circular track.
 * Your friend runs always faster than you.
 * Then there will be always a time when your friend will pass by you.
 * Based on the same logic, create slow and fast pointers. Fast will always go twice as fast as slow does. slow goes node by node.
 * 
 * At one point, if slow is equal to fast, that means a cycle is detected, because there is no way that a non-circular linked list will have fast and slow pointers pointing at the same node at the same time.  
 */
export function hasCycle(head: ListNode | null): boolean {
  let slow = head
  let fast = head

  while (fast && fast.next) {
    slow = slow?.next ?? null
    fast = fast?.next?.next ?? null

    if (slow === fast) {
      return true
    }
  }

  return false
};