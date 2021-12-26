from typing import List

def solution(n : int, money : List[int]) -> int:
    money.sort()
    combinations = [[] for i in range(n+1)] # leave idx 0 empty
    for coin in money:
        if coin <= n:
            combinations[coin].append((coin,))
    for idx in range(2,n+1):
        for coin in money:
            if idx - coin >= 1:
                for combi in combinations[idx-coin]:
                    combinations[idx] += [tuple(sorted((*combi, coin)))]
            elif idx < coin:
                break # next coins are definitely bigger
        combinations[idx] = list(set(combinations[idx]))
    return len(combinations[-1]) % 1000000007

cases = [(5, [1,2,5])]
for n, money in cases:
    print(solution(n, money))

