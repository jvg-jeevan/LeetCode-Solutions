class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = 1
        # mask generates number like 8 for 3 binary digits then 8-1 = 7 (111) and xor with given num gives complement
        while mask <= num:
            mask <<= 1
        return (mask-1) ^ num