from functools import reduce
from typing import List


class Solution:
    # O(N) time complexity
    # O(N) space complexity
    def singleNumber(self, nums: List[int]) -> int:
        nums_hash = {}
        for n in nums:
            if not n in nums_hash:
                nums_hash[n] = True
            else:
                del nums_hash[n]
        return list(nums_hash.keys())[0]

    def singleNumber_improved(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)