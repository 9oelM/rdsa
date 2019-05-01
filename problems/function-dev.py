# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# https://sunpil.tistory.com/40
# 100 = progresses[i] + speeds[i] * day
# ( 100 - progresses[i] ) / speeds[i] = day
def solution(progresses, speeds):
    from math import ceil
    daysNeeded = [ceil((100 - progress) / speeds[count]) for count, progress in enumerate(progresses)]
    ans = []
    while daysNeeded:
        first = daysNeeded.pop(0)
        count = 1
        while daysNeeded and first >= daysNeeded[0]:
            daysNeeded.pop(0)
            count += 1
        ans.append(count)
    return ans
