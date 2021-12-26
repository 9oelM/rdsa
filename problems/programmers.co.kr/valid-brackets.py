def solRecur(N, length, base=["()"]):
    N = N - 1
    if N == 0:
        return [s for s in base if len(s) == length*2]
    new = []
    for each in base:
        new.append(f'({each})')
        new.append(f'{each}()')
        new.append(f'(){each}')
    base += new
    base = list(set(base))
    return solRecur(N, length, base)

def solution(N):
    return solRecur(N, N)
    
print(solution(4))
"""
['(((())))', '(()(()))', '()()()()', '((()()))', '(()())()',
'()((()))', '()(()())', '()(())()', '(())()()', '(()()())', '((()))()', '()()(())', '((())())']
"""
