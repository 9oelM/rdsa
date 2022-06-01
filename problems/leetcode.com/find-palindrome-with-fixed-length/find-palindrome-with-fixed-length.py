from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
      assert intLength > 0, "intLength is bigger than 0"

      """
      As int length grows,
      the number of available palindromes also increases.

      # palindromes | intLength
      1 * 9            1 or 2
      10 * 9           3 or 4
      100 * 9          5 or 6
      ... and so on

      so we can get the power of 10 on the left side of the multiplication ('x' in 10^x * 9): namely, tens_power.

      Getting it is as simple as adding 1 to intLength if it is odd, and dividing it by 2 and subtracting 1 from it.

      There is also a formula to calculate the left half of the palindrome. The pattern can easily be detected when you review the palindromes of intLength up to 5 or 6 (try it yourself on this)

      This is the formula:

      left_half = query + 10^tens_power - 1      

      For example,

      if intLength == 5 and you are looking for 136th palindrome, 

      tens_power = ((5 + 1) / 2) - 1 = 2
      left_half = 136 + 10^tens_power - 1 = 136 + 10^2 - 1 = 235

      The left half is 235, so the right half must be 32 to make it into the palindrome.

      Therefore, 136th palindrome is 23532.
      """
      is_int_length_odd = intLength % 2 != 0
      if is_int_length_odd:
        intLength += 1 
      tens_power = (intLength // 2) - 1
      left_half_addition_factor = 10 ** tens_power
      number_of_available_palindromes = (10 ** tens_power) * 9
      
      answers = [-1] * len(queries)
    
      for (i, q) in enumerate(queries):
        if q <= number_of_available_palindromes:
          left_half = q + left_half_addition_factor - 1
          right_half_str = str(left_half)
          if is_int_length_odd:
            right_half_str = right_half_str[:len(right_half_str)-1][::-1]
          else:
            right_half_str = right_half_str[::-1]

          left_half_str = str(left_half)
          ans = f'{left_half_str}{right_half_str}'
          answers[i] = int(ans)

      return answers
