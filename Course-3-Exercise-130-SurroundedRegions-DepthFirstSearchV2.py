from collections import deque
from typing import List
from itertools import product


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1). retrieve all border cells
        borders = (list(product(range(self.ROWS), [0, self.COLS - 1]))
                   + list(product([0, self.ROWS - 1], range(self.COLS))))
        # borders = (list(product([0, self.COLS - 1], range(self.ROWS)))
        #            + list(product([0, self.ROWS - 1], range(self.COLS))))

        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for row, col in borders:
            self.BFS(board, row, col)

        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'

    def BFS(self, board, row, col):
        stack = deque([(row, col)])
        while stack:
            (row, col) = stack.pop()
            if board[row][col] != 'O':
                continue
            board[row][col] = 'E'
            if col < self.COLS - 1:
                stack.append((row, col + 1))
            if row < self.ROWS - 1:
                stack.append((row + 1, col))
            if col > 0:
                stack.append((row, col - 1))
            if row > 0:
                stack.append((row - 1, col))



if __name__ == '__main__':

    # Inputs and Expected Outputs
    board_1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected_output_1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]

    board_2 = [["X"]]
    expected_output_2 = [
        ["X"]
    ]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.solve(board_1)
    test_2 = solution_2.solve(board_2)

    # Print Results
    print(f"\nResult 1: {board_1} \nExpected Result: {expected_output_1}")
    print(f"\nResult 1: {board_2} \nExpected Result: {expected_output_2}")