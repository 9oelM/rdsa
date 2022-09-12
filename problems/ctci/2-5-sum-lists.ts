// https://leetcode.com/problems/add-two-numbers/solution/
export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

/**
 * Key to this problem: setting up a head that won't be included in the answer
 */
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const ansHead = new ListNode()
  let ptr = ansHead
  let carry = 0

  while (l1 !== null || l2 !== null || carry !== 0) {
    const tmpSum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry
    const onesDigit = tmpSum % 10
    carry = tmpSum >= 10 ? 1 : 0
    ptr.next = new ListNode(onesDigit)
    ptr = ptr.next
    l1 = l1?.next ?? null
    l2 = l2?.next ?? null
  }

  return ansHead.next
};