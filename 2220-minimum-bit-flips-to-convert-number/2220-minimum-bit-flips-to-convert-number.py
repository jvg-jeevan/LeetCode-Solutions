class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # the bits needed to be flipped given by xor
        res = start ^ goal
        res = bin(res)
        return res.count('1')