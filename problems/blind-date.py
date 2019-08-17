from typing import List, Tuple

def calcTempScore(crntTemp: int) -> Tuple[int, bool]:
    mightBeBadDay = crntTemp >= 30 or crntTemp <= 0
    return 20 - abs(22 - crntTemp), mightBeBadDay

def calcWeatherScore(skyStatusCode: int, rainFallStatusCode: int) -> Tuple[int, bool]:
    mightBeBadDay = skyStatusCode == 4 or rainFallStatusCode == 1
    score = -1
    if skyStatusCode <= 2:
        score = 20
    elif skyStatusCode == 3:
        score = 17
    elif skyStatusCode == 4:
        score = 10
    # For rainFall, do I just add with the score from skyStatusCode? There's no instruction on this.
    # I think the common sense is to say score is 5 if it's raining even though it's sunny
    if rainFallStatusCode == 1:
        score = 5
    elif rainFallStatusCode == 2:
        score = 14
    return score, mightBeBadDay

def calcScore(arr: List[int]) -> Tuple[int, bool]:
    tempScore, mightBeBadDay1 = calcTempScore(arr[2])
    weatherScore, mightBeBadDay2 = calcWeatherScore(arr[0], arr[1])
    return tempScore + weatherScore, mightBeBadDay1 or mightBeBadDay2

def solution(data: List[List[int]]) -> List[int]:
    dayPriority = [0,1,3,2,5,6,4] # 동점이면 토요일, 금요일, 일요일, 수요일, 목요일, 화요일, 월요일 순으로 우선권
    badDay = -1
    data = [(*calcScore(arr), idx) for idx, arr in enumerate(data)]
    data.sort(key=lambda tup: (tup[0], dayPriority[tup[2]]))
    if data[0][1]:
        badDay = data[0][2]
    return [data[-1][2], badDay]


testCases = [[[1, 0, 11], [3, 1, 15], [2, 0, 16], [4, 0, 17], [2, 0, 15], [2, 1, 14], [2, 0, 12]],
             [[3, 0, 20], [2, 1, 17], [3, 0, 17], [2, 0, 31], [1, 0, 19], [1, 0, 10], [4, 1, 14]],
             [[3, 0, 20], [2, 1, 17], [3, 0, 17], [2, 0, 31], [1, 0, 19], [1, 0, 19], [4, 1, 14]]]

for case in testCases:
    solution(case)
