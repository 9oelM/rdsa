# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

# brute forcing will take O(n^2) where n is len(nums)
# hash table will take O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, num in enumerate(nums):
          complement = target - num
          # there is exactly one solution, so there must be complement stored in nums list anyways
          # that means if we don't have the complement, we can pass it and that's not a solution
          # if we have the complement, that is directly going to be the solution
          if complement in hash_table:
            return [hash_table[complement], index]
          hash_table[num] = index

s = Solution()
print(s.twoSum([3,2,4], 6))