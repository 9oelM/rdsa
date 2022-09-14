// https://leetcode.com/problems/min-stack/
interface MinStackData<T> {
  data: T
  min: number
}

export class MinStack<T> {
  #arr: MinStackData<T>[] = []
  #min: number | null = null
  #processDataForMinFn: ((data: T) => number) | null = null

  constructor() {}

  public setProcessMin(processDataForMinFn: (data: T) => number) {
    this.#processDataForMinFn = processDataForMinFn
  }

  public push(item: T) {
    const itemval = (() => {
      if (typeof item === `number`) {
        return item
      } else if (!this.#processDataForMinFn) {
        throw new Error(`processDatForMinFn is null but item is not a number type`)
      } else {
        return this.#processDataForMinFn(item)
      }
    })()

    this.#arr.push({
      data: item,
      min: this.#min === null ? itemval : this.#min
    })

    this.#min = Math.min(this.#min ?? Number.POSITIVE_INFINITY, itemval)
  }

  public top(): T | null {
    if (this.#arr.length === 0) {
      return null
    }
    return this.#arr[this.#arr.length - 1].data
  }

  public pop(): null | T {
    const last = this.#arr.pop()

    if (!last) return null

    this.#min = last.min

    return last.data
  }

  public min(): number | null {
    return this.#min
  }
}
