// https://leetcode.com/problems/add-two-numbers-ii/
export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let l1Digit: ListNode | null = l1
  let l1Digits: number[] = l1 ? [] : [0]
  let l2Digit: ListNode | null = l2
  let l2Digits: number[] = l2 ? [] : [0]

  // because you don't know the length of each linked list, you must
  // reach the end of each first
  let ansLength = 0
  // O(max(len(l1)), max(len(l2)))
  while (l1Digit !== null || l2Digit !== null) {
    if (l1Digit) l1Digits.push(l1Digit.val)
    l1Digit = l1Digit?.next ?? null
    if (l2Digit) l2Digits.push(l2Digit.val)
    l2Digit = l2Digit?.next ?? null
    ++ansLength
  }

  console.log(l1Digits)
  console.log(l2Digits)
  console.log(ansLength)

  let carry = 0
  // + 1 for a possible carry
  let ansArrayLen = ansLength + 1
  let ansArray = new Array<ListNode>(ansArrayLen); 
  
  // O(max(len(l1)), max(len(l2)))
  for (let i = 0; i < ansArrayLen; ++i) {
    ansArray[i] = new ListNode();
    if (i !== 0 && i < ansArrayLen) {
      ansArray[i - 1].next = ansArray[i]
    }
  }

  console.log(ansArray)

  // O(max(len(l1)), max(len(l2)))
  while (ansLength >= 0 || carry !== 0) {
    const tmpSum = (l1Digits.pop() ?? 0) + (l2Digits.pop() ?? 0) + carry
    ansArray[ansLength].val = tmpSum % 10
    carry = tmpSum >= 10 ? 1 : 0
    --ansLength
  }

  console.log(carry)
  console.log(ansLength)
  console.log(ansArray)

  if (ansArray[0].val === 1) {
    return ansArray[0]
  }
  return ansLength === -1 ? ansArray[1] : ansArray[0]
};

