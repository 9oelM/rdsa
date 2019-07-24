# https://programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    works.sort()
    for _ in range(n):
        if works[-1] == 0:
            break
        i = len(works) - 1
        while works[i] != 0:
            if works[i] != 0:
                works[i] -= 1
                break 
            else:
                i -= 1
            
        w = works[-1]
        for j in reversed(range(len(works))):
            if w < works[j]:
                works = works[:j-1] + [w] + works[j-1:-1]
                break
    
    return sum([elem ** 2 for elem in works])

testcases = [(4, [4, 3, 3]), (1, [2,1,2]), (3, [1,1])]

for n, works in testcases:
    print(solution(n, works))
    print('----')
