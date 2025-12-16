class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        # calculate the no of rows= m and no of columns= n values
        m, n = len(matrix), len(matrix[0])

        # calculate low, high index 
        low, high = 0, (m*n) - 1
        
        while low <= high:
            mid = (low+high) // 2
            # to get the row and col of the mid index
            row = mid // n
            col = mid % n
            # same as binary search
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                high = mid-1
            else:
                low = mid+1
        return False