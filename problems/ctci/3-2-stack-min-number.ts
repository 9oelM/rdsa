// https://leetcode.com/problems/min-stack/
/**
 * ## Workflow
 * 
 * push: push the value and the current minimum together into the array, so that the latest minimum will
 * always stay at the top of the stack. O(1) time.
 * 
 * pop: just pop. the second to the last element will already contain the next min number. O(1) time.
 * 
 * getMin: just access the `min` of the last element. It will already contain the latest min value. O(1) time.
 */
export class MinStack {
  private arr: {
      data: number;
      min: number;
  }[] = []
  
  constructor() {}


  push(val: number): void {
    this.arr.push({
      data: val,
      min: Math.min(this.getMin(), val),
    })
  }

  pop(): void {
    this.arr.pop()
  }

  top(): number {
    if (this.arr.length === 0) {
      return Number.MAX_SAFE_INTEGER
    }
    return this.arr[this.arr.length - 1].data
  }

  getMin(): number {
    return this.arr[this.arr.length - 1]?.min ?? Number.MAX_SAFE_INTEGER
  }
}