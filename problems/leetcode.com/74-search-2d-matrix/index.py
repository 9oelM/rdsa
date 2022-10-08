from typing import List, Tuple


class Solution:
#         """
#         1. merge all the subarrays and then run binary search
#         'merge' part
#         - O(n) time
#         - O(n) space
        
#         'binary search' part
#         - O(logn) time
#         - O(1) space
        
#         O(n + logn) time
#         O(n)? space

#         2. directly go into binary search and figure out indices wisely during the binary search
#         - O(logn) time
#         - O(1) space
#         """
    def searchMatrix0(self, arr: List[int], target: int) -> int:
        """
        1 2 3 4 5 6
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return -1 if arr[left] != target else arr[left]
    
    def calc_oned_and_twod_indices(self, matrix_length: int, subarray_length: int, flattened_oned_index: int) -> Tuple[int, int]:
        oned_index = flattened_oned_index % subarray_length
        twod_index = flattened_oned_index // subarray_length
        
        return (oned_index, twod_index)
    
    def searchMatrix1(self, arr: List[List[int]], target: int) -> bool:
        if len(arr) == 0 or len(arr[0]) == 0:
            raise Exception(f"matrix does not meet the requirement of the problem")
        
        subarray_length = len(arr[0])
        matrix_length = len(arr)
        total_length = matrix_length * subarray_length
        
        oned_left, oned_right = 0, total_length - 1
        
        while oned_left < oned_right:
            oned_mid = oned_left + (oned_right - oned_left) // 2
            oned_mid_inside_subarray, twod_mid = self.calc_oned_and_twod_indices(matrix_length, subarray_length, oned_mid)
            if arr[twod_mid][oned_mid_inside_subarray] >= target:
                oned_right = oned_mid
            else:
                oned_left = oned_mid + 1
        oned_left_inside_subarray, twod_left = self.calc_oned_and_twod_indices(matrix_length, subarray_length, oned_left)
        
        return arr[twod_left][oned_left_inside_subarray] == target
