# https://programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    works.sort()
    for _ in range(n):
        if works[-1] == 0:
            break
        for i in reversed(range(len(works))):
            if i - 1 != -1 and works[i] > works[i-1]: # not the first element
                works[i] -= 1
                break
            elif i == 0: # the first element. This is the smallest elem
                works[i] -= 1
    return sum([elem ** 2 for elem in works])

testcases = [(4, [4, 3, 3]), (1, [2,1,2]), (3, [1,1])]

for n, works in testcases:
    print(solution(n, works))
    print('----')
