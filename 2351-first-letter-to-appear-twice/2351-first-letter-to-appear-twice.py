class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = [0] * 26
        for i in s:
            count[ord(i)-97] += 1
            if count[ord(i)-97] >= 2:
                return i