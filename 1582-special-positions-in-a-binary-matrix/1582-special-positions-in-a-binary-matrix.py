class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [0] * m
        cols = [0] * n
        # count number of 1's in rows and cols
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res