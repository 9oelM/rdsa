from collections import defaultdict
from typing import List

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than 
⌊n / 2⌋ times. 
You may assume that the majority element 
always exists in the array.
"""

low_bound = -10**9

class Solution:
    # O(N) time, O(N) space
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)
        nums_len = len(nums)
        for n in nums:
          nums_count[n] += 1
          if nums_count[n] > nums_len // 2:
            return n

        return -1
    
    # O(nlogn) time, O(1) space
    def majorityElement_nlogn(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # O(N) time, O(1) space
    # Boyer-Moore Voting Algorithm
    def majorityElement_best(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

s = Solution()
s.majorityElement_best([2,2,1,1,1,2,2])