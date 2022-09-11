// see https://leetcode.com/problems/partition-list/
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
 class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
  }
}
/**
* Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
* You should preserve the original relative order of the nodes in each of the two partitions.
*/
function partition(head: ListNode | null, x: number): ListNode | null {
let ptr: ListNode | null = head

const tmpNodes: Record<string, ListNode | null> = {
  lessThanX: null,
  lessThanXFirstNode: null,
  greaterThanX: null,
  greaterThanXFirstNode: null
} 
while (ptr !== null) {
    if (ptr.val < x) {
      if (tmpNodes.lessThanX) {
        tmpNodes.lessThanX.next = ptr
      }
      else {
        tmpNodes.lessThanXFirstNode = ptr
      }
      tmpNodes.lessThanX = ptr
    } else {
      if (tmpNodes.greaterThanX) {
        tmpNodes.greaterThanX.next = ptr
      }
      else {
        tmpNodes.greaterThanXFirstNode = ptr
      }
      tmpNodes.greaterThanX = ptr
    }
    ptr = ptr.next
}
if (tmpNodes.greaterThanX?.next) {
  tmpNodes.greaterThanX.next = null
}
if (tmpNodes.lessThanX) {
  tmpNodes.lessThanX.next = tmpNodes.greaterThanXFirstNode
}

return tmpNodes.lessThanXFirstNode ?? tmpNodes.greaterThanXFirstNode
};