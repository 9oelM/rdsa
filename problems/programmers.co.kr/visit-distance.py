from typing import List, Tuple

def go(crntLocation: Tuple[int, int], dirs: str, isVisitedTo: List[List[int]], count: int) -> int:
    x, y = crntLocation
    for c in dirs:
        prevX, prevY = x, y
        if c == 'U' and y + 1 <= 10:
            y += 1
        elif c == 'R' and x + 1 <= 10:
            x += 1
        elif c == 'D' and y - 1 >= 0:
            y -= 1
        elif c == 'L' and x - 1 >= 0:
            x -= 1

        if (prevX, prevY) not in isVisitedTo[x][y] and (x, y) not in isVisitedTo[prevX][prevY] and (x,y) != (prevX, prevY):
           # print(f'{prevX - 5}, {prevY - 5} -> {x - 5},{y - 5}')
            isVisitedTo[x][y].append((prevX, prevY))
            isVisitedTo[prevX][prevY].append((x, y))  # it's bidirectional
            count += 1

    return count


def solution(dirs):
    # -5 -4 -3 -2 -1 0 1 2 3 4 5
    #  0  1  2  3  4 5 6 7 8 9 10
    isVisitedTo = [[[] for i in range(11)] for j in range(11)]

    answer = go((5, 5), dirs, isVisitedTo, 0)
    return answer


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
