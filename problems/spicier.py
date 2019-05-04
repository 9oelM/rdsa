def solution(scoville, K):
    scoville.sort()
#    print(scoville)
    scv, cnt = 0, 0
    while len(scoville) >= 1 and scv <= K:
        scv = scoville.pop(0) + scoville[0] * 2
        scoville[0] = scv
      #  print(scoville)
        scoville.sort()
        cnt += 1
    return cnt
    """ 
    from heapq import heapify, heappop, heappush
    heapify(scoville)
    print(scoville)
    scv, cnt = 0, 0
    while len(scoville) >= 1 and scv <= K:
        scv += heappop(scoville) + scoville[0] * 2
        scoville[0] = scv
        print(scoville)
        cnt += 1
    return cnt"""
