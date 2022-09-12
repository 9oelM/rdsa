// https://leetcode.com/problems/palindrome-linked-list/
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
 * 
 * - space: O(1)
 * - time: O(n)
 * 
 * ## Workflow
 * 
 * 1. Have two pointers travel from the head of the linked list.
 * One ('slow') will visit the nodes one by one, the other will go twice as fast ('fast').
 * The moment the faster node reaches the end means the 'slow' node will be at the middle
 * 
 * 2. While the slow node travels, it is possible to reverse the direction of the linked list.
 * Do that.
 * 
 * 3. After the traversal, just move pointer on each separate linked list from the middle,
 * one to the left and the other one to the right. Check if the data from each pointer is the same as the other for every move. If they are not the same at any point, the linked list does not contain a palindrome
 */
function isPalindrome(head: ListNode | null): boolean {
  let fastPtr: ListNode | null = head
  let slowPtr: ListNode | null = head
  let prevSlowPtr: ListNode | null = null
  let rightSideNextPtr: ListNode | null = null
  while ((fastPtr?.next ?? null) !== null) {
    fastPtr = fastPtr?.next?.next ?? null
    rightSideNextPtr = slowPtr?.next ?? null
    if (slowPtr) slowPtr.next = prevSlowPtr
    prevSlowPtr = slowPtr
    slowPtr = rightSideNextPtr
  }
  const isOddLength = fastPtr !== null
  
  if (isOddLength) {
    rightSideNextPtr = rightSideNextPtr?.next ?? null
  }
  while (prevSlowPtr !== null && rightSideNextPtr !== null) {
    if (rightSideNextPtr.val !== prevSlowPtr.val) return false
    rightSideNextPtr = rightSideNextPtr.next
    prevSlowPtr = prevSlowPtr.next
  }

  return true
};
