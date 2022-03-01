# problem: https://leetcode.com/problems/container-with-most-water/
# solution video: https://youtu.be/UuiTKBwPgAo

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
import sys
from typing import List

# two important things in this qs:
# 1. the length between the two heights
# 2. the vertical heights of the two heights 
# formulae: (i1 - i0) * min(heights[i0], heights[i1]), and i just need to find the biggest value out of this

# Approach 1. bruteforcing:
# iterate height list two times in a nested for loop
# gives O(n^2) where n = len(heights)
def bruteforce(heights: List[int]) -> int:
  area = 0

  for left_height_i, left_height in enumerate(len(heights)):
    for right_height_i, right_height in range(1 + 1, len(heights)):
      area = max(min(right_height, left_height) * (right_height_i - left_height_i), area)

  return area

"""
Approach 2. linear time solution
Two-pointer solution.
At the beginning, we want the width to be as big as possible, so we start from the very left and right.

The gist of the problem lies in the fact that each bar can essentially can have two areas, each on left and right.
The maximum area a single bar can achieve is its min(its own height, any other bars height) * remaining horizontal space.

Because the area is limited by the minimum height between the two bars, it's essential to eliminate the lower bar and move inwards from that direction to find a higher bar. For example, if a left bar is 4m tall and right 6m, move inwards from left, in the hope for finding a bar that's greater than 6m. It's okay to remove the lower bar because it won't be a solution anyway, because a lower bar cannot produce an area greater than the higher bar.
"""
class Solution:
  def solve_plainly(self, heights: List[int]) -> int:
    area, left, right = 0, 0, len(heights) - 1

    while left < right:
      area = max(area, (right - left) * min(heights[left], heights[right]))

      if heights[left] < heights[right]:
        left += 1
      else:
        right -= 1

    return area
  """
  This recursive solution will take larger memory than a plain iterative solution because new stack frames need to be added for every single function call above the previous one.
  It could possibly take more execution time too.
  """
  def solve_recursively(self, left: int, right: int, heights: List[int], current_max: int) -> int:
    # the right bar can't get left to the left bar
    if left >= right:
      return current_max

    area = max(current_max, (right - left) * min(heights[left], heights[right]))

    next_left, next_right = (left + 1, right) if heights[left] < heights[right] else (left, right - 1)

    return self.solve_recursively(next_left, next_right, heights, area)

  def maxArea(self, heights: List[int]) -> int:
    return self.solve_recursively(0, len(heights) - 1, heights, 0)

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
