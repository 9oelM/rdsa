export class LinkedListNode<Data> {
  public data: Data
  public next?: LinkedListNode<Data>
  public index?: number
  constructor(data: Data, index?: number, next?: LinkedListNode<Data>) {
    this.data = data
    this.next = next
    this.index = index
  }
}

export class LinkedList<Data> {
  public head: LinkedListNode<Data>

  constructor(...initData: Data[]) {
    if (initData.length === 0) {
      throw new Error(`initData must be more than 0`)
    }

    // to avoid typing head as undefined
    this.head = new LinkedListNode<Data>(initData[0], 0) 
    let current: LinkedListNode<Data> | undefined = this.head
    initData.forEach((data, i) => {
      if (i === 0) {
        return
      }
      else if (current) { 
        current.next = new LinkedListNode<Data>(data, i)
        current = current.next
      }
    })
  }
  
  public printLinkedList<Data>(head?: LinkedListNode<Data>) {
    let ptr: LinkedListNode<Data> | undefined = head 
    while (ptr !== undefined) {
      console.log(ptr.data)
      ptr = ptr.next
    }
  }
}

