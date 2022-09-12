// https://leetcode.com/problems/palindrome-linked-list/
export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function isPalindrome(head: ListNode | null): boolean {
  const numbers: number[] = []

  while (head !== null) {
    numbers.push(head.val)

    head = head.next
  }

  for (let i = 0; i < numbers.length / 2; i++) {
    if (numbers[i] !== numbers[numbers.length - 1 - i]) {
      return false
    }
  }

  return true
};