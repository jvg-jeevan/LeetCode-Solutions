class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len not equal return false
        if len(s) != len(t):
            return False
        # if anagram all counts must be 0
        count = [0] * 26
        for i, j in zip(s, t):
            count[ord(i)-97] += 1
            count[ord(j)-97] -= 1
        return all(c==0 for c in count)