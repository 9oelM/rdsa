# https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    from heapq import heapify, heappop, heappush
    heapify(scoville)
    cnt = 0
    while scoville[0] <= K:
        try:
            heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
            cnt += 1
        except: 
            # you might get an error trying to pop from the heap for the second time. If this happens, 
            # it's already the case that you are running out of elements, 
            # but you still can't make all food's scoville indices larger than K.
            return -1
    return cnt 
