import sys
from typing import List

def solution(n : int, costs : List[List[int]]) -> int:
    
    costsArray = [[0 for _ in range(n)] for __ in range(n)]
    for cost in costs:
        costsArray[cost[0]][cost[1]] = cost[2]
        costsArray[cost[1]][cost[0]] = cost[2]


    for islandNum in range(n):
        print('-----')
        nxtIdx, minCost = islandNum, 0
        visited = [False] * n
        visited[islandNum] = True
        for _ in range(n-1):
            
            minimum = islandNum, sys.maxsize
            for idx, elem in enumerate(costsArray[nxtIdx]):
                if elem < minimum[1] and elem != 0 and not visited[idx]:
                    minimum = idx, elem
                    
            print(minimum)
            nxtIdx = minimum[0]
            minCost += minimum[1]
            visited[nxtIdx] = True
        
    return minCost
    

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
