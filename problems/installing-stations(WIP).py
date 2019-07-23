# https://programmers.co.kr/learn/courses/30/lessons/12979

def forward(station, w, until, last=False):
    stationCount = 0
    while station + w * 2 + 1 <= until:
        stationCount += 1
        station = station + w * 2 + 1
    # last right edge
    if station + w + 1 <= until and last:
        stationCount += 1
    return stationCount

def backward(station, w, until, last=False):
    stationCount = 0
    while station - w * 2 + 1 >= until:
        stationCount += 1
        station =  station - w * 2 + 1 
    # last left edge
    if station - w - 1 >= until and last:
        stationCount += 1
    return stationCount 

def solution(n, stations, w):
    leftRightWidth = w * 2 + 1
    stationLen = len(stations)
    stationCount = 0
    stations.sort()
    for idx, s in enumerate(stations):
        station = s
        if idx == 0:
            stationCount += backward(s, w, 1, True)
            if stationLen == 1: # only one station
                stationCount += forward(s,w,n, True)
        else:
            if idx != stationLen - 1: # not the last APT
                stationCount += forward(s,w,stations[idx+1])
            else: # last APT
                stationCount += forward(s,w,n, True)
    return stationCount
