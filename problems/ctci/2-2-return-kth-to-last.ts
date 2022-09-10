import { LinkedList, LinkedListNode } from './linkedlist';

function returnKthToLastNode<Data>(linkedList: LinkedList<Data>, k: number): LinkedListNode<Data> | undefined {
  if (k <= 0) {
    throw new Error(`k must be larger than 0`)
  }
  let ptr0: LinkedListNode<Data> | undefined = linkedList.head
  let ptr1: LinkedListNode<Data> | undefined = linkedList.head
  
  for (let i = 0; i < k; i++) {
    // move ptr0 by k
    ptr0 = ptr0 ? ptr0.next : undefined
  }
  // the length of linkedList is shorter than k
  if (ptr0 === undefined) return undefined

  // move ptr0 to the end
  while (ptr0 !== undefined) {
    ptr0 = ptr0 ? ptr0.next : undefined
    // move ptr1 by n - k
    ptr1 = ptr1 ? ptr1.next : undefined
  }

  return ptr1
}

console.log(returnKthToLastNode(new LinkedList(1,2,3,4,5,6,7,8,9,10), 4))
console.log(returnKthToLastNode(new LinkedList(1,2,3,4,5,6,7,8,9,10), 1))
console.log(returnKthToLastNode(new LinkedList(1,2,3,4,5,6,7,8,9,10), 10))