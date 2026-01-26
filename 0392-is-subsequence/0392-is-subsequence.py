class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # try matching char in longest string t with each in s
        m, n = len(t), len(s)
        i, j = 0, 0
        # if the matching is complete then the value of j will be equal to len of s
        # if not subsequence then the length will be lesser
        while i < m and j < n:
            if s[j] != t[i]:
                i += 1
            else:
                i += 1
                j += 1
        return j == n