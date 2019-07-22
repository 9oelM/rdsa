# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    result = {('||', 2), ('=', 2)}
    if n == 1:
        return 1 
    elif n == 2:
        return 2
    else:
        ans = set()
        for i in range(n-2):
            newSet = set()
            for arrangement, width in result:
                if width + 1 <= n:
                    newSet.add((f'{arrangement}|', width + 1))
                    newSet.add((f'|{arrangement}', width + 1))
                if width + 2 <= n:
                    newSet.add((f'{arrangement}=', width + 2))
                    newSet.add((f'={arrangement}', width + 2))
            result |= newSet
            result = set([(arrangement, width) for arrangement, width in result if n - width <= 2])
    count = sum(width == n for arrangement, width in list(result))
    return count

print(solution(4))
