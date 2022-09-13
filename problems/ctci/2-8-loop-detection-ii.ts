// https://leetcode.com/problems/linked-list-cycle-ii/

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
 * - time: O(n) (don't know)
 * - space: O(1)rdsa
 * 
 * ## Workflow
 * Suppose your friend and you are running on the same, circular track.
 * Your friend runs always faster than you.
 * Then there will be always a time when your friend will pass by you.
 * Based on the same logic, create slow and fast pointers. Fast will always go twice as fast as slow does. slow goes node by node.
 * 
 * At one point, if slow is equal to fast, that means a cycle is detected, because there is no way that a non-circular linked list will have fast and slow pointers pointing at the same node at the same time.  
 */
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function hasCycle(head: ListNode | null): ListNode | null { 
  let slow = head
  let fast = head
  
  while (fast && fast.next) {
    fast = fast.next.next
    slow = slow?.next ?? null

    if (fast == slow) {
      return fast  
    }
  }

  return null
}

/**
 * ## Complexity
 * - time: O(n)
 * - space: O(1)
 * 
 * ## Workflow
 * Now we understand the logic behind `hasCycle`. 
 * Then we need to think about how to get the entry node to the cycle.
 * 
 * Detailed explanation: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44781/Concise-O(n)-solution-by-using-C%2B%2B-with-Detailed-Alogrithm-Description
 */
export function detectCycle(head: ListNode | null): ListNode | null {
  let maybeNodeInLoop = hasCycle(head)

  if (!maybeNodeInLoop) return null

  while (maybeNodeInLoop != head) {
    // practically, it never becomes null because there is a cycle
    maybeNodeInLoop = maybeNodeInLoop?.next ?? null;
    head = head?.next ?? null;
  }
  return head;
};