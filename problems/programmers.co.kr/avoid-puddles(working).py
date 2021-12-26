
from typing import List

def solution(width : int, height : int, obstacles : List[List[int]]) -> int:
    grid = [[0 for y in range(height + 1)] for x in range(width + 1)]
    for puddle in obstacles:
        grid[puddle[0]][puddle[1]] = -1
    grid[1][1] = 1
    for x in range(width + 1):
        for y in range(height + 1):
            if grid[x][y] != -1:
                if grid[x][y-1] != -1:
                    grid[x][y] += grid[x][y-1]
                if grid[x-1][y] != -1:
                    grid[x][y] += grid[x-1][y]
                grid[x][y] = grid[x][y] % 1000000007
    return grid[-1][-1]

print(solution(4,3, [[2,2]]))