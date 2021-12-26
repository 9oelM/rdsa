# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/submissions/

# Inefficient solution
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr = [[x,y] for x in nums1 for y in nums2]
        arr.sort(key=lambda arr : sum(arr))
        return arr[:k]
 
# Efficient solution
class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        idx1, idx2 = 0, 0
        ans = []
        ans.append([nums1[idx1], nums2[idx2]])
        