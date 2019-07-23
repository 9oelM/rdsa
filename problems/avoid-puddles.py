# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(width, height, obstacles):
    markedMap = [[0 for i in range(width)] for j in range(height)]
    markedMap[0][0] = 1
    for obstacle in obstacles:
        markedMap[obstacle[0]-1][obstacle[1]-1] = -1
    for i in range(height):
        for j in range(width):
            if markedMap[i][j] != -1:
                if i - 1 >= 0 and markedMap[i-1][j] != -1:
                    markedMap[i][j] += markedMap[i-1][j] % 1000000007
                if j - 1 >= 0 and markedMap[i][j-1] != -1:
                    markedMap[i][j] += markedMap[i][j-1] % 1000000007
    return markedMap[-1][-1]

print(solution(4,3,[[2,2]]))
