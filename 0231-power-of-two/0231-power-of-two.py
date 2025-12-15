class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # # if num < 0 not a power of 2
        # if n <= 0:
        #     return False
        # # if power of 2 then n will become 1
        # if n == 1:
        #     return True
        # # if odd then cannot be
        # if n % 2 != 0:
        #     return False
        # # right shift then // 2
        # return self.isPowerOfTwo(n >> 1)

        # if it is power of two then not(n & (n-1)) will result in True or else False
        return n > 0 and not(n & (n - 1))