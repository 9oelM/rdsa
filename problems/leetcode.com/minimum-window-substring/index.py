from collections import defaultdict
from typing import Dict

def minimum_window_substring(s: str, substr: str) -> str:
  substr_hash: Dict[str, int] = defaultdict(int)
  window_hash: Dict[str, int] = defaultdict(int)

  # for "ABCDAB", need_unique_chars_count will be 4 because A and B overlap
  # it's just len(substr_hash)
  need_unique_chars_count = 0
  for c in substr:
    if substr_hash[c] == 0: need_unique_chars_count += 1
    substr_hash[c] += 1

  have_unique_chars_count = 0
  minimum_window_bounds = [-1, -1]
  start = 0
  # initiate 'end' from the beginning of the string
  for end in range(len(s)):
    if s[end] in substr_hash:
      window_hash[s[end]] += 1
      if window_hash[s[end]] == substr_hash[s[end]]:
        have_unique_chars_count += 1
      # minimum requiremenet to create a window
      # for this char has been fulfilled
    # the condition to create a valid sliding window has
    # been fulfilled
    while have_unique_chars_count == need_unique_chars_count:
      curr_window_size = end - start + 1
      # current valid window size is smaller than the existing one
      # therefore we need to replace the window
      if minimum_window_bounds[0] == -1 or curr_window_size < minimum_window_bounds[1] - minimum_window_bounds[0] + 1:
        minimum_window_bounds = [start, end]
      # keep shrinking from the left
      window_hash[s[start]] -= 1
      # if you happen to take out the character
      # that was required for the minimum window,
      # decrement have_unique_chars_count by 1
      if s[start] in substr_hash and window_hash[s[start]] < substr_hash[s[start]]:
        have_unique_chars_count -= 1
      start += 1
  if minimum_window_bounds[0] == -1:
    return ""
  return s[minimum_window_bounds[0]:minimum_window_bounds[1] + 1]
