/**
 * Three in one: describe how you could use a single array to implement three stacks
 * 
 * ## Kinds of implementations
 * 
 * 
 */

class NStacksInArray<T> {
  private arr: Array<T> = []
  private lastIndices: Array<number> = []
  private prevIndices: Array<number> = []
  private nStacks: number;

  constructor(n: number, defaultVal: T | null = null) {
    this.nStacks = n
    for (let i = 0; i < n; i++) {
      // dummy head node
      this.arr.push()
      // prev node (it itself is a dummy node, and .next holds the ref to the prev node)
      this.arr.push()
    }
  }

  public push(item: T, whichStack = 0): void {
    if (whichStack >= this.nStacks) {
      throw new Error(`Stack ID can't be bigger than or equal to ${this.nStacks}`)
    }
    this.arr.push()
  }
  
  public peek(whichStack = 0): T | null {
    if (whichStack >= this.nStacks) {
      throw new Error(`Stack ID can't be bigger than or equal to ${this.nStacks}`)
    }

  }

  public pop(whichStack = 0): T | null {
    return re
  }
}