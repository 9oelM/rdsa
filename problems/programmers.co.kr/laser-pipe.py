# https://programmers.co.kr/learn/courses/30/lessons/42585
#                   "( ) ( ( ( ( ) ( ) ) ( ( ) )  (  )  )  )  (  (  )  ) "
# pipeCnt         0  0   1 2 3 3   3   2 3 3   2  2     1  0  1  1     0 0 
# totalPipeCount  0  0   0 0 0 3   6   7 7 10  11 13    14 15 15 16   16 17
def solution(arrangement):
    L, R, pipeCount, totalPipeCount= "(", ")", 0, 0
    arrangement = list(arrangement)
    while len(arrangement) > 1:
        bracket = arrangement.pop(0)
        nxtBracket = arrangement[0]
        if bracket == L:
            if nxtBracket == R: # laser
                totalPipeCount = pipeCount + totalPipeCount
                arrangement.pop(0)
            else: # not a left side of laser
                pipeCount = pipeCount + 1
        else: # not laser, just the end of pipe
            pipeCount = pipeCount - 1
            totalPipeCount = 1 + totalPipeCount
    return totalPipeCount + 1 # cuz it ended when len(arrangement) is still 1
