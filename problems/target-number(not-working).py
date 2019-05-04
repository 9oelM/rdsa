# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def dfs(total : int, numbers : int, target : int):
    if numbers:
        num = numbers.pop(0) # this part does not work properly. Have to use array concatenation
        return dfs(-num+total, numbers, target) + dfs(num+total, numbers, target)
    else:
        return 1 if total == target else 0
