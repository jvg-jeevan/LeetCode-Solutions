class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        rows = [''] * numRows
        cur_row = 0
        direction = -1
        
        for ch in s:
            rows[cur_row] += ch

            if cur_row == 0 or cur_row == numRows-1:
                direction *= -1
            
            cur_row += direction
        
        return ''.join(rows)