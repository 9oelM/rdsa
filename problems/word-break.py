# https://leetcode.com/problems/word-break/
# could'nt solve it
# trying to explain it with one of the best solution
from typing import List

def wordBreak(s : str, words: List[str]) -> bool:
    ok = [True]
    max_len = max(map(len,words+[''])) # addding [''] just in case?
    print(max_len) # the longest word's length
    words = set(words) # sift out duplicates
    for i in range(1, len(s)+1): # for each letter in string
        # add to array "ok" 
        ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
    return ok[-1]
 
if __name__ == "__main__":
    print(wordBreak("applepenapple", ["apple", "pen"]))
    print(wordBreak("leetcode", ["leet", "code"]))
    print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
