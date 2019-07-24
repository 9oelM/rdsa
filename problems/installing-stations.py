# https://programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
    idx, location, count = 0, 1, 0
    while location <= n:
        if idx < len(stations) and stations[idx] - w <= location: # current location is inside the range of a nearby station, so there's no need to install another
            # jump over that station
            location = stations[idx] + w + 1
            idx += 1
        else: # you are not in the range of a nearby station. Install one. 
            count += 1
            location += 2 * w + 1
    return count

print(solution(11, [4,11], 1))
print(solution(16, [9], 2))
print(solution(9, [], 2))


print(solution(11, [4,11], 1))
print(solution(16, [9], 2))
print(solution(9, [], 2))
