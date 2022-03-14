# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int, left: int, right: int):
      m = (left + right) // 2
      if left == right:
        return -1
      if nums[m] > target:
        return self.binary_search(nums, target, left, m)
      elif nums[m] < target:
        return self.binary_search(nums, target, m + 1, right)
      else:
        return m

    def search(self, nums: List[int], target: int) -> int:
      return self.binary_search(nums, target, 0, len(nums))

s = Solution()
print(s.search([-1,0,3,5,9,12], 111))
print(s.search([-1,0,3,5,9,12], 12))
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 5))
print(s.search([-1,0,3,5,9,12], 3))
print(s.search([-1,0,3,5,9,12], 0))
print(s.search([-1,0,3,5,9,12], -1))
