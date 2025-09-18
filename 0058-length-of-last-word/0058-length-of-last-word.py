class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings = s.strip().split(" ")
        res = 0
        for i in strings[-1]:
            res += 1
        return res