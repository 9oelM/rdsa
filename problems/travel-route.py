# https://programmers.co.kr/learn/courses/30/lessons/43164

from typing import List

def canVisit(t1 : List[str], t2 : List[str], lastDest : str):
    """
    Returns whether you can travel from t1[1] to t2[0].
    Also checks the route is kept unbroken by checking t1[0] == lastDest.
    """
    return t1[1] == t2[0] and t1[0] == lastDest

def getRoute(tickets : List[str], ans : str = "ICN"):
    """
    returns the route starting from 'ans'.
    """
    if len(tickets) == 1: 
        return f'{ans},{tickets[0][1]}'.split(",")
    else:
        for i in range(1,len(tickets)): # for each ticket, check connectivity with tickets[0]
            if canVisit(tickets[0], tickets[i], ans[-3:]): # there is a connected route 
                t = tickets.pop(0)
                return getRoute(tickets, f'{ans},{t[1]}') # choose the first one that works
    # if there is no connected route at all from tickets[0], mix the ticket around (send it to the back) to keep exploring
    return getRoute(tickets[1:] + tickets[:1], ans) 

def comparator(arr : List[List[str]]):
    """
    returns the item (array) of higher alphabetical order.
    """
    if len(arr) == 1: # if there's only one route, just return that route
        return arr[0]

    length = len(arr[0])
    best = arr[0]
    for i in range(1,len(arr)):
        for k in range(length):
            if best[i] > arr[i][k]:
                best = arr[i]
                break
    return best

def initialize(tickets : List[List[str]]):
    tickets.sort(key=lambda x : x[0] == "ICN", reverse=True)
    startCnt = 0
    for x in tickets:
        if x[0] == "ICN":
            startCnt += 1
        else:
            break
    return tickets, startCnt

def solution(tickets):
    tickets, startCnt = initialize(tickets)
    
    ansPool = []
    for i in range(startCnt):
        t = tickets.pop(0)
        ansPool.append(getRoute([t]+tickets))
        tickets.append(t)
    return comparator(ansPool)
