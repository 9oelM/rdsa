def solution(N : int, number : int) -> int:
    # It's the 'minimum'. Don't forget this.
    num = number
    combinations = []
    for usedNum in range(2, 9):
        combinations += [num + number, num - number, num * number, num / number]
        combinations += [num + num2, ]
        combinations

    return -1 # not found