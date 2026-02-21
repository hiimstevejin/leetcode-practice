# backtracking question.
# define a backtracking function solve() which will look at each element in the board and try to fill it with a valid number.
# if the current square is ".", try to fill it with a number and check is_valid to see if the board is still valid.
# invoke solve inside to start the backtracking process. it will fill the other squares recursively. Comeback to this question later I need deeper understanding of backtracking.
#


class Solution:
    def solveSudoku(self, board):
        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in "123456789":
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        solve()
