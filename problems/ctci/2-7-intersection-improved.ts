export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

export function findTailAndLength(head: ListNode | null): {
    tail: ListNode | null
    len: number
} {
    let len = 0
    while (head !== null) {
        head = head.next
        ++len
    }

    return {
        tail: head, len
    }
}

/**
 * ## Complexity
 * - time: O(n)
 * - space: O(1)
 * 
 * ## Workflow
 * 1. Find the tail and length of each list
 * 2. If two lists intersect somewhere, the tail must be the same
 * 3. One list may be longer than the other. Advance the pointer from the head of the longer list
 * by the difference in the length.
 * 4. Then, advance the pointer from the longer list and that from the head of the shorter list.
 * there must be a time when two pointers share the same reference
 */
export function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    const { tail: tailA, len: lenA } = findTailAndLength(headA)
    const { tail: tailB, len: lenB } = findTailAndLength(headB)

    if (tailA !== tailB) return null

    let lenDiff = Math.abs(lenA - lenB)

    while (lenDiff--) {
        if (lenA > lenB) {
            headA = headA?.next ?? null
        } else {
            headB = headB?.next ?? null
        }
    }

    while (headA !== headB) {
        headA = headA?.next ?? null
        headB = headB?.next ?? null
    }

    return headA
};