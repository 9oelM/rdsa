from math import inf
import sys
from typing import List, Union

def find_max_index(arr: List[int], tracking_index: int) -> int:
  if tracking_index == 0:
    return 0

  maybe_max_index = find_max_index(arr, tracking_index - 1)
  if arr[tracking_index] < arr[maybe_max_index]:
    return maybe_max_index
  return tracking_index

def selection_sort_recursive(arr: List[int], i: Union[int, None] = None) -> List[int]:
  """
  find the largest number in A[:i + 1] and swap it to A[i]
  """
  if i is None:
    i = len(arr) - 1

  if i == 0:
    return arr

  max_index = find_max_index(arr, i)
  arr[i], arr[max_index] = arr[max_index], arr[i]
  return selection_sort_recursive(arr, i - 1)

def selection_sort(arr: List[int]) -> List[int]:
  """
  sort i items from the end, and decrease i until 1
  """
  # if [9,7,6,4,1], then i would enumerate as 4,3,2,1
  for i in range(len(arr) - 1, 0, -1):
    # if i = 4, then j would enumerate as 0,1,2,3
    largest_j = i
    for j in range(i):
      if arr[largest_j] < arr[j]:
        largest_j = j
    arr[largest_j], arr[i] = arr[i], arr[largest_j]
  return arr

def insert_last(arr, i):
  if i > 0 and arr[i] < arr[i - 1]:
    arr[i], arr[i - 1] = arr[i - 1], arr[i]
    insert_last(arr, i - 1)

def insertion_sort_recursive(arr: List[int], i = None):
  """
  """
  if i is None:
    i = len(arr - 1)
  if i > 0:
    insertion_sort_recursive(arr, i - 1)
    insert_last(arr, i)

def insertion_sort(arr: List[int]) -> List[int]:
  """
  sort i items from the beginning, and increase i until len(arr)
  """
  for i in range(1, len(arr)):
    j = i
    # swap all until arr[j] < arr[j - 1] 
    while j > 0 and arr[j] < arr[j - 1]:
      arr[j - 1], arr[j] = arr[j], arr[j - 1]
      j = j - 1
  return arr

def merge(arr0: List[int], arr1: List[int]) -> List[int]:
  i = len(arr0) - 1
  j = len(arr1) - 1
  current_insertion_index = len(arr0) + len(arr1) - 1
  merged_sorted_list = [None] * (len(arr0) + len(arr1))

  while (i >= 0 or j >= 0) and current_insertion_index >= 0:
    # -1 means the list has run out of elements already
    if (arr0[i] > arr1[j] and i != -1) or j == -1:
      merged_sorted_list[current_insertion_index] = arr0[i]
      i -= 1
    elif j != -1 or i == -1:
      merged_sorted_list[current_insertion_index] = arr1[j]
      j -= 1
    current_insertion_index -= 1

  return merged_sorted_list

# left, right: all inclusive
def merge_sort(arr: List[int], left: int, right: int) -> List[int]:
  # if 4 elements, then (0 + 3 + 1) // 2 = 2
  # if 5, (0 + 4 + 1) // 2 = 2
  middle = (left + right) // 2
  if left == right and middle == right:
    return [arr[middle]]
  arr0 = merge_sort(arr, left, middle)
  arr1 = merge_sort(arr, middle + 1, right)
  return merge(arr0, arr1)

def direct_access_array_sort():
  
  pass

def tuple_sort():
  pass

def counting_sort():
  pass

def radix_sort():
  pass


a = [1,2,3,5,7,8,9,0,2,1,4,5,1,5,1,32,4]
print(merge_sort(a, 0, len(a) - 1))
# merge_sort([1,2,3,4], 0, 3)

print(merge([1,2,3], [4,5,6]))
print(merge([2,4,5], [4,5,6]))
print(merge([4,7,7], [4,5,8]))
print(merge([4,7,7], [4,5]))