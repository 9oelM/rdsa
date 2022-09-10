class LinkedListNode<Data> {
  public data: Data
  public next?: LinkedListNode<Data>
  public index?: number
  constructor(data: Data, index?: number, next?: LinkedListNode<Data>) {
    this.data = data
    this.next = next
    this.index = index
  }
}

function removeDupsWithNoBuffer<Data>(head: LinkedListNode<Data> | undefined) {
  let curr: LinkedListNode<Data> | undefined = head
  while (curr !== undefined) {
    let runner: LinkedListNode<Data> | undefined = curr
    while (runner.next !== undefined) {
      if (runner.next.data === curr.data) {
        // delete data
        runner.next = runner.next.next
      } else {
        runner = runner.next
      }
    }
    curr = curr.next
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
  initData.forEach((data, i) => {
    if (!current) {
      current = new LinkedListNode<Data>(data, i)
      head = current
    }
    else { 
      current.next = new LinkedListNode<Data>(data, i)
      current = current.next
    }
  })

  return head
}

function printLinkedList<Data>(head?: LinkedListNode<Data>) {
  let ptr: LinkedListNode<Data> | undefined = head 
  while (ptr !== undefined) {
    console.log(ptr.data)
    ptr = ptr.next
  }
}

const head = createLinkedList(1,1,1,1,2,2,2,2,2,3,33,33,4,1,1,4,4,4,41,2,1,3,1,1) as LinkedListNode<number>
printLinkedList(head)

removeDupsWithNoBuffer(head)
console.log(`-----------------`)
printLinkedList(head)