# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 100 = progresses[i] + speeds[i] * day
# ( 100 - progresses[i] ) / speeds[i] = day
def solution(progresses, speeds):
    from math import ceil
    from functools import reduce
    daysNeeded = [ceil((100 - progress) / speeds[count]) for count, progress in enumerate(progresses)]
    ans = []
    counter = 1
    while(daysNeeded):
        first = daysNeeded.pop(0)
        if daysNeeded:
            maximum = max(first, daysNeeded[0])
            if maximum == first:
                counter += 1
            else:
                ans.append(counter)
                counter = 1
        else:
            ans.append(counter)        
    return ans
