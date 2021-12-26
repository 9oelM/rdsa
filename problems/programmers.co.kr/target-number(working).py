from typing import List

def dfs(total : int, numbers : List[int], target : int, index : int):
    if len(numbers) >= index + 1:
        return dfs(total-numbers[index], numbers, target, index+1) + dfs(total+numbers[index], numbers, target, index+1)
    else:
        return 1 if total == target else 0
    
def solution(numbers, target):
    return dfs(0, numbers, target, 0)
