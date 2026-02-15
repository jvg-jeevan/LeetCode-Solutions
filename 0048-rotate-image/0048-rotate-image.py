class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1. transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse_row(row):
            left = 0
            right = len(row)-1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

        # reverse each row
        for row in matrix:
            reverse_row(row)