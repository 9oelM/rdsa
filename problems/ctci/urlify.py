from typing import List


SPACE_SIGN = "%20"
REVERSED_SPACE_SIGN = reversed(SPACE_SIGN)

a = "AB CD  EF      "
# a = "AB CD  EF EF"
# a = "AB CD%20%20EF"
# slen - len_space_at_end = 12 - 3 = 9
# 9 - 1 = 8

# O(N) time complexity
# O(1) space complexity
def urlify(slist: List[str], true_len: int) -> str:
  slen = len(slist)
  len_space_at_end = slen - true_len

  space_count = 0
  offset_from_end = 0
  for i in range(slen - len_space_at_end - 1, -1, -1): # O(N)
    if slist[i] == " ":
      space_count += 1
    else:
      if current_space_count > 0:
        for j in range(len(REVERSED_SPACE_SIGN) *  current_space_count): 
          slist[slen - 1 - offset_from_end] = REVERSED_SPACE_SIGN[j % len(REVERSED_SPACE_SIGN)]
          offset_from_end += 1
        current_space_count = 0

      slist[slen - 1 - offset_from_end] = slist[i]
      offset_from_end += 1

  return ''.join(slist)

def urlify_cleaner_version(slist: List[str], true_len: int) -> str:
  slen = len(slist)
  len_space_at_end = slen - true_len

  space_count = 0
  offset_from_end = 0
  for i in range(slen - len_space_at_end - 1, -1, -1): # O(N)
    if slist[i] == " ":
      space_count += 1
  for i in range(slen - len_space_at_end - 1, -1, -1): # O(N)
    if slist[i] == " ": 
      slist[slen - 1 - offset_from_end] = "0"
      slist[slen - 1 - offset_from_end - 1] = "2"
      slist[slen - 1 - offset_from_end - 2] = "%"
      offset_from_end += 3
      space_count -= 1
    else:
      slist[slen - 1 - offset_from_end] = slist[i]
      offset_from_end += 1

  return ''.join(slist)

print(urlify_cleaner_version(list(a), 9))