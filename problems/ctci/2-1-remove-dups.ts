class LinkedListNode<Data> {
  public data: Data
  public next?: LinkedListNode<Data>
  constructor(data: Data, next?: LinkedListNode<Data>) {
    this.data = data
    this.next = next
  }

  public toString(): string {
    return `{ data: ${this.data}, next: [${this.next ? `LinkedListNode` : `undefined`}]`
  }
}

function removeDups<Data>(head: LinkedListNode<Data>) {
  let next: LinkedListNode<Data> | undefined = head
  let prev: LinkedListNode<Data> | undefined = undefined
  const hash: Record<string, boolean> = {}
  while (next !== undefined) {
    if (JSON.stringify(next.data) in hash) {
      next = removeNode(next, prev)
    }
    else {
      hash[JSON.stringify(next.data)] = true
      prev = next
      next = next.next
    }
  }
}

function removeNode<Data>(curr: LinkedListNode<Data>, prev?: LinkedListNode<Data>) {
  if (prev) {
    prev.next = curr.next
  }

  return prev ? prev.next : undefined
}

function createLinkedList<Data>(...initData: Data[]): LinkedListNode<Data> | undefined {
  let current: LinkedListNode<Data> | undefined = undefined
  let head: LinkedListNode<Data> | undefined = undefined
  initData.forEach((data) => {
    if (!current) {
      current = new LinkedListNode<Data>(data)
      head = current
    }
    else { 
      current.next = new LinkedListNode<Data>(data)
      current = current.next
    }
  })

  return head
}

function printLinkedList<Data>(head?: LinkedListNode<Data>) {
  let ptr: LinkedListNode<Data> | undefined = head 
  while (ptr !== undefined) {
    console.log(ptr)
    ptr = ptr.next
  }
}

const head = createLinkedList(1,2,3,4,5,6,7,8,8,8,9,9,9,1,2) as LinkedListNode<number>
printLinkedList(head)

removeDups(head)
console.log(`-----------------`)
printLinkedList(head)