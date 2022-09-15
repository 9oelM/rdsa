function findAndCutMiddle(head: ListNode | null): ListNode | null {
  let fast: ListNode | null = head
  let slow: ListNode | null = head
  let prevSlow: ListNode | null = null
  while (fast && fast.next) {
      fast = fast.next.next
      prevSlow = slow
      slow = slow?.next ?? null
  }
  const isOddLength = fast !== null
  const slowNext = slow?.next

  if (prevSlow && !isOddLength) prevSlow.next = null
  if (slow && isOddLength) slow.next = null
  
  const middleNode = isOddLength ? (slowNext ?? null) : slow
  return middleNode
}

function reverseList(head: ListNode | null): ListNode | null {
  let curr = head
  let prev = null
  let next = null

  while (curr) {
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }

  return prev
}

function reorderList(head: ListNode | null): void {
  const middleNode = findAndCutMiddle(head)
  let rightHead = reverseList(middleNode)
  while (rightHead) {
    const nextHead = head?.next ?? null
    const nextRightHead = rightHead?.next ?? null
  
    if (head) head.next = rightHead 
    if (rightHead) rightHead.next = nextHead
  
    head = nextHead
    rightHead = nextRightHead
  }
};
