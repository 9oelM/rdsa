# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    # O(n) Time, O(1) Space solution
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(k) < O(n) time
        for i in range(k):
          nums[i], nums[-k+i] = nums[-k+i], nums[i]

        middle_elements_num = len(nums) - 2 * k
        interchange_elements_num = min(middle_elements_num, k)

        print(nums)

        # O(min(middle_elements_num, k)) < O(n) time
        for i in range(interchange_elements_num):
          nums[k + i], nums[-k + i] = nums[-k + i], nums[k + i]

        print(nums)
        print(interchange_elements_num,)
        # O(k) < O(n) time
        for i in range(k - 1):
          before = k + interchange_elements_num + i
          after = k + interchange_elements_num + i + 1
          nums[before], nums[after] = nums[after], nums[before] 
        
s = Solution()
a = [1,2,3,4,5,6,7]
s.rotate(a, 3)
b = [1,2,3,4,5,6,7]
s.rotate(b, 2)
c = [1,2,3,4,5,6,7]
s.rotate(c, 1)
a1 = [-1,-100,3,99]
s.rotate(a1, 2)

print(a)
print(b)
print(c)
