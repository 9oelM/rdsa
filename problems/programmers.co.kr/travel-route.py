# https://programmers.co.kr/learn/courses/30/lessons/43164
from typing import List
def canVisit(t1 : List[str], t2 : List[str], lastDest : str):
    return t1[1] == t2[0] and t1[0] == lastDest

def getRoute(tickets : List[str], ans : str = "ICN"):
    if len(tickets) == 1: 
        return f'{ans},{tickets[0][1]}'.split(",")
    else:
        for i in range(1,len(tickets)): # for each ticket, check connectivity with tickets[0]
            if canVisit(tickets[0], tickets[i], ans[-3:]): # there is a connected route 
                t = tickets.pop(0)
                return getRoute(tickets, f'{ans},{t[1]}') # choose the first one that works
    return getRoute(tickets[1:] + tickets[:1], ans) 

def initialize(tickets : List[List[str]], startPoint: str):
    tickets.sort(key=lambda x : x[0] == startPoint, reverse=True)
    startCnt = 0
    for x in tickets:
        if x[0] == startPoint:
            startCnt += 1
        else:
            break
    return tickets, startCnt

def solution(tickets):
    tickets, startCnt = initialize(tickets, "ICN")
    ansPool = []
    for i in range(startCnt):
        t = tickets.pop(0)
        ansPool.append(getRoute([t]+tickets))
        tickets.append(t)
    return min(ansPool)
