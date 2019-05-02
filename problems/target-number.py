# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def bfs(total, numbers : int, target : int):
    if total == target: # found
        print('found')
        return 1
    if total > target or (total < target and not numbers): # not found. Halt searching.
        print('not found')
        return 0    
    num = numbers.pop()
    bfs(-num+total, numbers, target)
    bfs(num+total, numbers, target)

print(bfs(0, [1,1,1,1,1], 3)) # should be 5
