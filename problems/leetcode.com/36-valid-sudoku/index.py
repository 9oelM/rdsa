from typing import List, Tuple


class Solution:
    def update_bits_and_check_dup(self, curr: int, left_shift_bits: int) -> Tuple[int, bool]:
        prev = curr
        curr |= (1 << left_shift_bits)
        # prev == curr means we have a duplicate number
        return (curr, prev == curr)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each elem represents a column 
        cols: List[int] = [0] * 9
        # each elem represents a square in 
        three_horizontal_squares = [0] * 3
        for row_index, row in enumerate(board):
            # represents current row
            curr_row = 0
            if row_index % 3 == 0: three_horizontal_squares = [0] * 3
            for col_index, n in enumerate(row):
                if n == ".": continue
                int_n = int(n)
                if int_n < 1 or int_n > 9: raise Exception(f"a number in Sudoku must be between 1 and 9 but received {int_n}")

                square_index = col_index // 3
                updated_bits, has_duplicates = tuple(zip(*map(lambda val: self.update_bits_and_check_dup(val, int_n), [
                    three_horizontal_squares[square_index],
                    cols[col_index],
                    curr_row,  
                ])))

                if any(has_duplicates): return False

                three_horizontal_squares[square_index], cols[col_index], curr_row = updated_bits
        return True