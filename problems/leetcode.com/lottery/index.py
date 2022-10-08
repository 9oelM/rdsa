from collections import defaultdict
from email.policy import default
from typing import Dict, List


def lottery_coupons(n: int) -> int:
  """
  largest group of people = number of digits in an n

SUMS
front\back 
     0  1  2   3  4 5 6 7 8 9   10   11

0    X  1  2   3  4 5 6 7 8 9   1    2  
1    1  2  3   4  5 6 7 8 9 10  2    3 
2    2  3  4   5  6 7 8 9 10 11 3    4 
3    3  4  5   6                4    5 
4    4  5
5    5
6
7
8
9 
10
11
12

  3 peeps
  """
  num_counter: Dict[int, int] = defaultdict(int)
  
  largest_count = 0
  largest = -1
  for i in range(1, n + 1): # <-- improve
    summed = sum(map(lambda num_str: int(num_str), list(str(i))))
    num_counter[summed] += 1
    prev_largest = largest 
    largest = max(largest, num_counter[summed])
    if prev_largest == largest:
      largest_count += 1
    else:
      largest_count = 1
  return largest_count

# print(lottery_coupons(12))
# print(lottery_coupons(23))
# print(lottery_coupons(33))
# print(lottery_coupons(41))
print(lottery_coupons(110))
# print(lottery_coupons(240))

def count_sentences(word_set: List[str], sentences: List[str]) -> List[int]:
  """
  "eilstn": [listen, slient],
  "it": [it],
  "is": [is]
  """
  anagrams: Dict[str, set] = defaultdict(set)
  
  for word in word_set:
    anagrams["".join(sorted(word))].add(word)

  ans: List[int] = []
  for sentence in sentences:
    words = set(sentence.split(" "))
    curr_ans = 1
    for word in words:
      sorted_word = "".join(sorted(word))
      if sorted_word in anagrams:
        curr_ans *= len(anagrams[sorted_word])
    ans.append(curr_ans)
  return ans

wordSet = ['listen', 'silent', 'it', 'is'] 
sentence = ["listen it is silent"]
print(count_sentences(wordSet, sentence))