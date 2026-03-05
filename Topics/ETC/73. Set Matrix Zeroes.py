class Solution:
    # O(1) Solution
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False # Does the first row need to be zeroed?

        # 1. Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Mark the column
                    if r > 0:
                        matrix[r][0] = 0 # Mark the row
                    else:
                        row_zero = True

        # 2. Use markers to fill zeros (skip first row/col for now)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 3. Handle the first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 4. Handle the first row
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                curr = matrix[i][j]
                if curr == 0:
                    q.append((i,j))

        while q:
            r,c = q.popleft()
            for i in range(ROWS):
                matrix[i][c] = 0
            for j in range(COLS):
                matrix[r][j] = 0
