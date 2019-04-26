# https://bubobubo003.tistory.com/44
# https://programmers.co.kr/learn/courses/30/lessons/42578/
def solution(clothes):
    from collections import Counter
    c = Counter([cloth[1] for cloth in clothes])
    ans = 1
    for x in c.values():            
        ans *= (x+1) 
        # add 1 because you need to account for 
        # not wearing some category at all (it is going to be factored into
        # other combinations that do not have this category of cloth. 
    return ans - 1 # -1 for ignoring wearning no clothes at all
