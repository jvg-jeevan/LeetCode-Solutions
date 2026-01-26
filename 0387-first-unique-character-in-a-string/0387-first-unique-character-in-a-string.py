class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i])-97] += 1
        
        for i in range(len(s)):
            if count[ord(s[i])-97] == 1:
                return i
        return -1