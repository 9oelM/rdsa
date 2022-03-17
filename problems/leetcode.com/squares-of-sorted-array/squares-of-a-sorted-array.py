# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [None]*len(nums)
        i = len(nums) - 1

        if len(nums) == 1:
          return [nums[0]**2]

        while i >= 0:
          left_squared, right_squared = nums[left]**2, nums[right]**2
          if left_squared >= right_squared:
            result[i] = left_squared
            left += 1
          else:
            result[i] = right_squared
            right -= 1
          i -= 1

        return result

s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))