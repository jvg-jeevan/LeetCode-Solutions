class Solution:
    def myAtoi(self, s: str) -> int:
        i, res = 0, 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < n and s[i] == " ":
            i += 1
        
        if i == n:
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            if res > INT_MAX//10  or (res == INT_MAX//10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            res = digit + (res*10)
            i += 1
        
        return sign * res