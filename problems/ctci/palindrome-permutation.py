"""
The catch is that if there is more than one character 
that appear only once in the string, 
the string can't make a palindrome.

example:

"Tact Coa",
- t, a, c appear twice (more than twice also doesn't matter)
- o only appears once
- this is still Ok. Can make a palindrome
- ignore whitespace and casing (as described by the qs)
- return True (ex. TACOCAT)

"TactbfCoa"
- t, a, c appear twice (more than twice also doesn't matter)
- b, o, and f appear only once
- this is not ok because there are more than or 
  equal to two characters that only appear once in the string
- return False (ex. best we can do is TACOBFCAT)

"""
from functools import reduce
from typing import Dict
def has_palindrome(s: str) -> bool:
  if len(s) == 1:
    return True

  chars: Dict[str, int] = {}

  for c in s:
    lc = c.lower()
    if lc == " ":
      continue
    if not (lc in chars):
      chars[lc] = 1
    else:
      chars[lc] += 1

  number_of_chars_appearing_once = 0
  # O(len(s))
  for (_, v) in chars.items():
    if v == 1:
      number_of_chars_appearing_once += 1
      if number_of_chars_appearing_once >= 2:
        return False

  return True 

def has_palindrome_improved(s: str) -> bool:
  chars: Dict[str, int] = {}

  for c in s:
    lc = c.lower()
    if lc == " ":
      continue
    if not (lc in chars):
      chars[lc] = True
    else:
      del chars[lc]

  return len(chars.keys()) <= 1

cases = [
  "Tact Coa",
  "TactbfCoa",
  "a",
  "ab",
  "abb"
]

for c in cases:
  print(has_palindrome(c))
for c in cases:
  print(has_palindrome_improved(c))