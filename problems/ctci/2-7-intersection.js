export function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * ## Complexity
 * - time: O(len(headA) + len(headB))
 * - space: O(len(headA))
 */
export var getIntersectionNode = function(headA, headB) {
    while (headA !== null) {
        headA.visited = true
        headA = headA.next
    }

    while (headB !== null) {
        if ('visited' in headB) {
            return headB
        }
        headB = headB.next
    }
    
    return null
};