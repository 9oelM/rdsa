# https://programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
    if not stations:
        count = 0
        count += n // (2 * w + 1)
        re = n % (2 * w + 1)
        if re > 0:
            count += 1
        return count
    
    stationLen = len(stations)
    stationCount = 0
    stations.sort()
    left = stations[0] - w
    while left > 0:
        stationCount += 1
        left -= 2 * w + 1
    for idx in range(len(stations)):
        if idx + 1 != len(stations):
            diff =  stations[idx+1] - stations[idx] - 2 * w
            while diff > 0:
                stationCount += 1
                diff -= 2 * w + 1
    right = n - stations[-1] - w
    while right > 0:
        stationCount += 1
        right -= 2 * w + 1
    return stationCount

print(solution(11, [4,11], 1))
print(solution(16, [9], 2))
print(solution(9, [], 2))
