from math import ceil
from typing import List


class Solution:
  """
  Given a list of unique words, return all the pairs of the distinct indices (i, j)
  in the given list, 
  so that the concatenation of the two words words[i] + words[j] is a palindrome.
  """
  def palindromePairs(self, words: List[str]) -> List[List[int]]: