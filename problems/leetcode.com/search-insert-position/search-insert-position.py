from typing import List

class Solution:
    def binary_search(self, nums, target, left, right) -> int:
      if left >= right:
        return left

      m = (left + right) // 2
      if nums[m] > target:
        return self.binary_search(nums, target, left, m)
      elif nums[m] < target:
        return self.binary_search(nums, target, m + 1, right)
      else:
        return m

    def searchInsert(self, nums: List[int], target: int) -> int:
      return self.binary_search(nums, target, 0, len(nums))  