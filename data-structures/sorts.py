from math import inf
from pprint import pprint
import sys
import types
from typing import List, Type, Union

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
  i, j = len(arr0) - 1, len(arr1) - 1 
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

def merge_sort_improved(arr: List[int], left = 0, right = None):
  if right is None:
    right = len(arr)
  if 1 < right - left:
    center = (left + right + 1) // 2
    merge_sort_improved(arr, left, center)
    merge_sort_improved(arr, center, right)
    left_array, right_array = arr[left:center], arr[center:right]
    i, j = 0, 0
    while left < right:
      if (j > len(right_array)) or (i < len(left_array) and left_array[i] < right_array[j]):
        arr[left] = left_array[i]
        i += 1
      else:
        arr[left] = right_array[j]
        j += 1
      left += 1

def direct_access_array_sort(arr: List[int]) -> List[int]:
  """
  Note: only small numbers
  """
  daa = [None] * (max(arr) + 1)
  for _, elem in enumerate(arr):
    daa[elem] = elem
  return [x for x in daa if x is not None]

def tuple_sort(arr: List[int]):


  pass

def counting_sort(arr: List[int]) -> List[int]:
  new_arr = [[] for _ in range(max(arr) + 1)]
  for _, elem in enumerate(arr):
    new_arr[elem].append(elem)
  sorted_array = []
  for chain in new_arr:
    for elem in chain:
      sorted_array.append(elem)

  return sorted_array

class Box: 
  key = None
  item = None
  digits = None

  def __str__(self) -> str:
    return f"Box{{digits: {self.digits} item: {self.item}}}"

def counting_sort_box(arr: List[Type[Box]]) -> List[Type[Box]]:
  new_arr = [[] for _ in range(max([x.key for x in arr]) + 1)]
  for _, elem in enumerate(arr):
    new_arr[elem.key].append(elem)
  
  i = 0
  for chain in new_arr:
    for elem in chain:
      arr[i] = elem
      i += 1

  return arr

def radix_sort(arr: List[int]):
  # the length of the original array
  n = len(arr)
  max_element_value = 1 + max(arr)
  # c = length of a digit tuple
  # dividing bit length of max_element_value by the length of the original array and adding one
  # gives the number of digits that can represent the numbers in the original array in base n
  c = 1 + (max_element_value.bit_length() // n.bit_length())
  print(f"{c} = 1 + ({max_element_value.bit_length()} // {n.bit_length()})")
  D = [Box() for a in arr]

  # prepare digits to be sorted, in a particular base
  for i in range(n):
    D[i].digits = []
    D[i].item = arr[i] # to be accessed for later
    high = arr[i]
    for j in range(c):
      # x // y, x % y = divmod(x, y)
      high, low = divmod(high, n)
      D[i].digits.append(low)

  for d in D:
    print(d)
  # sort from least significant to most significant digit
  for i in range(c):
    for j in range(n):
      D[j].key = D[j].digits[i]
    counting_sort_box(D)
    # print(f"{i}th counting sort")
    # for d in D:
    #   print(d)

  # output item in the original array
  for i in range(n):
    arr[i] = D[i].item
  return arr

# print(radix_sort([10,22,22,53,26,63,17,39,99,55]))
# print(radix_sort([134,9,1245,112,90]))
# print(radix_sort([112,134,1245,61,63,919,41,9]))
# print(radix_sort([112,134,1245,61,63,919,41,8,9]))
# print(radix_sort([1251251,1122315]))

