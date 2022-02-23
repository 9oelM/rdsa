from typing import List, Tuple
import unittest

from sorts import selection_sort_recursive, selection_sort, insertion_sort, merge, merge_sort

def create_testcases():
  tests: Tuple[Tuple[List[int], List[int]]] = [
      (
          [1,2,3,4,5],
          [1,2,3,4,5]
      ),
      (
          [5,4,3,2,1],
          [1,2,3,4,5]
      ),
      (
          [4,4,4,3,3],
          [3,3,4,4,4]
      ),
      (
          [2,1],
          [1,2]
      ),
      (
          [1,1],
          [1,1]
      ),
      (
          [112,134,1245,61,63,919,41,9],
          [ 9, 41, 61, 63, 112, 134, 919, 1245 ]
      ),
      (
        [1,4,5,7,8,9,1,5,6,7,8,9,1,12,45,5,7,8,9,877,1,14,6,78,2,1,1,14,2],
        [
          1,   1, 1, 1, 1,  1,  2,  2,  4,
          5,   5, 5, 6, 6,  7,  7,  7,  8,
          8,   8, 9, 9, 9, 12, 14, 14, 45,
          78, 877
        ]
      ),
      (
        [9,7,6,5,4,3,2,1,1,2,5,6,7,71241,5616,67,1,1248,9,902,12,125],
        [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 7, 9, 9, 12, 67, 125, 902, 1248, 5616, 71241],
      )
      (
        [1],
        [1],
      ),
      (
        [2,1],
        [1,2],
      ),
      (
        [1,2],
        [1,2],
      )
  ]
  return tests

class TestCases(unittest.TestCase):
    def test_sorts(self):
      for description, fn in (
        (
          "recursive selection sort",
          selection_sort_recursive,
        ),
        (
          "selection sort",
          selection_sort,
        ),
        (
          "insertion sort",
          insertion_sort,
        ),
        (
          "merge sort",
          merge_sort,
        )
      ):
        for input, expected in create_testcases():
          if description == "merge sort":
            self.assertEqual(fn(input, 0, len(input) - 1), expected, f"{description} should sort correctly")
          else:
            self.assertEqual(fn(input), expected, f"{description} should sort correctly")
    def test_merge(self):
      merge_testcases = (
        (
          ([1,2,3], [4,5,6], [1,2,3,4,5,6]),
          ([2,4,5], [4,5,6], [2,4,4,5,5,6]),
          ([4,7,7], [4,5,8], [4,4,5,7,7,8]),
          ([4,7,7], [4,5], [4,4,5,7,7]),
          ([1], [1], [1,1]),
          ([2], [1], [1,2]),
          ([1], [2], [1,2]),
        )
      )
      for arr1, arr2, expected in merge_testcases:
        self.assertEqual(merge(arr1, arr2), expected, "merge should merge two sorted lists properly")

if __name__ == '__main__':
   unittest.main()
