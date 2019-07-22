from typing import List

def solution(n : int, money : List[int]) -> int:
    dp = [{(0,)}] * (n + 1) # if n = 5, len(dp) = 6
    numberOfWays = 0
    for i, elem in enumerate(dp):
        print(dp)
        for coin in money:
            if i + coin <= n:
                newTups = [list(set(sorted((*tup, coin)))) for idx, tup in enumerate(dp[i]) if sum((*tup, coin)) == i + coin]
                for tup in newTups:
                    dp[i+coin].add(tuple(tup))
                    print(f'inserting {tuple(tup)} at {i+coin}')
    return len(dp[n])

    
cases = [(5, [1,2,5])]
for n, money in cases:
    print(solution(n, money))

