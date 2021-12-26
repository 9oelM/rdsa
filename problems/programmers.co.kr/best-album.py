# https://programmers.co.kr/learn/courses/30/lessons/42579

from typing import List

def solution(genres : List[str], plays : List[int]) -> List[int]:
    store = {}
    rank = {}
    for gen, play in zip(genres, plays):
        if gen in rank:
            rank[gen] += play
        else:
            rank[gen] = play
    combined = sorted([[idx, *(genre, play)] for idx, (genre, play) in enumerate(zip(genres, plays))], key=lambda x : (rank[x[1]], x[1], x[2], -x[0]))
    answer = []
    for item in reversed(combined):
        idx, gen, play = tuple(item)
        if gen in store:
            if store[gen] < 2:
                store[gen] += 1
                answer.append(idx)
        else:
            store[gen] = 1
            answer.append(idx)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 500, 200]))
