# https://programmers.co.kr/learn/courses/30/lessons/43163

def isDiffByOneLetter(s1 : str, s2 : str) -> bool:
    count = 0
    for idx, letter1 in enumerate(s1):
        if s2[idx] != letter1:
            count += 1
        if count >= 2:
            return False
    if count == 0:
        return False
    return True

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = [begin]
    visited = [begin]
    prevQueueLen = 1
    count = 0
    while queue:
        nxt = []
        for _ in range(prevQueueLen):
            nxt.append(queue.pop(0))
        visited += nxt
        oneLetterDiffWords = []
        for nxtStr in nxt:
            oneLetterDiffWords += list(filter(lambda s2 : isDiffByOneLetter(nxtStr, s2) and s2 not in visited, words))
        prevQueueLen = len(oneLetterDiffWords)
        count += 1
        if target in oneLetterDiffWords:
            break
        queue += oneLetterDiffWords

    return count
