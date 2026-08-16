class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        left = 0
        visited = set()
# right to iterate
        for right in range(len(s)):
# if char already in visited then remove all the occurrence and keep incrementing left
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
# if char is not visited then add
            visited.add(s[right])
# get the max of lengths of the substring
            res = max(res, right - left + 1)
        
        return res