// https://leetcode.com/problems/add-two-numbers-ii/
export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
/**
 * You are given two non-empty linked lists representing two non-negative integers. 
 * The most significant digit comes first and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * 
 * The key to solving this problem is to use recursion, because it is hard to
 * crack this question without it.
 * 
 * Because the direction of the linked lists is defined in a way that the one's digit is at the head of the list, it will be easier to use recursion that would do something like `addLists(l1.next, l2.next)`.
 * 
 * Workflow
 * 1. Because two lists may not have the equal length, fill the list with shorter length with
 * 0's so that the length of each lists is the same
 * 2. Add the lists recursively in the way that the carry and the tail will be recursively returned
 */
export function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let l1Tail = l1
  let l2Tail = l2
  let l1Len = 0
  while (l1 !== null) {
    l1 = l1.next
    ++l1Len
  }
  let l2Len = 0
  while (l2 !== null) {
    l2 = l2.next
    ++l2Len
  }
  let lenDiff = Math.abs(l1Len - l2Len)

  while (lenDiff--) {
    if (l1Len - l2Len >= 0) {
      l2Tail = insertBefore(l2Tail)
    } else {
      l1Tail = insertBefore(l1Tail)
    }
  }

  const ans = addListsRecursively(l1Tail, l2Tail)
  
  if (ans.carry) {
    return insertBefore(ans.sum, 1)
  }
  return ans.sum
};

/**
 * Both lists need to have the same length
 */
export function addListsRecursively(l1: ListNode | null, l2: ListNode | null): {
  carry: number
  sum: ListNode | null
} {
  if (l1 === null || l2 === null) {
    return {
      sum: null,
      carry: 0,
    }
  }
  const tmpSum = addListsRecursively(l1.next, l2.next)
  const sum = (l1.val + l2.val) + tmpSum.carry

  return {
    sum: new ListNode((sum % 10), tmpSum.sum),
    carry: sum >= 10 ? 1 : 0
  }
}

export function insertBefore(tail: ListNode | null, val = 0): ListNode | null {
  const tmpPtr = new ListNode(val, tail)
  return tmpPtr
}