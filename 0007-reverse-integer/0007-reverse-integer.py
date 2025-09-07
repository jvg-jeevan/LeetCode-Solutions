class Solution:
    def reverse(self, x: int) -> int:
        num = 0

        # if x is -ve take sign as -1 and later xly with num
        sign = 1
        if x<0:
            sign = -1
            x *= -1

        while x > 0:
            # take remainder and xly with 10 and add to num
            num = (num * 10) + (x%10)
            x //= 10

        num *= sign
        
        # check if num exceeds 32 bits
        if (num > (2**31 - 1)) or (num < (-2**31)):
            return 0
        return num