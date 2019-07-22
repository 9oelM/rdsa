# https://programmers.co.kr/learn/courses/30/lessons/42886?language=python3
# https://oneshottenkill.tistory.com/377

def solution(weight):
    weight.sort()
    length=len(weight)
    s=1
    for i in range(length):
        if s<weight[i]:
            break
        s+=weight[i]
    return s


print(solution([3, 1, 6, 2, 7, 30, 1]))
