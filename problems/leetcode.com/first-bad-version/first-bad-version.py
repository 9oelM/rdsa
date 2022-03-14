# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
  pass

class Solution:
    def search(self, left: int, right: int) -> int:
      if left == right:
        return left
      middle = (left + right) // 2
      if isBadVersion(middle):
        return self.search(left, middle)
      else:
        return self.search(middle + 1, right)

    def firstBadVersion(self, n: int) -> int:
      return self.search(1, n)
