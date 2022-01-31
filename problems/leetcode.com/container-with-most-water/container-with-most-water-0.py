# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
from typing import List

# two important things in this qs:
# 1. the length between the two heights
# 2. the vertical heights of the two heights 
# formulae: (i1 - i0) * min(heights[i0], heights[i1]), and i just need to find the biggest value out of this

# bruteforcing:
# iterate height list two times in a nested for loop
# gives O(n^2) where n = len(heights)

# the gist of the problem lies in the fact that each bar can essentially can have two areas, each on left and right.
# the maximum area a single bar can achieve is its min(its own height, any other bars height) * remaining horizontal space
# this suggests that we might get the job done in O(n) time, where n = len(heights)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1

        for i, height in enumerate(heights):
          height



s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
