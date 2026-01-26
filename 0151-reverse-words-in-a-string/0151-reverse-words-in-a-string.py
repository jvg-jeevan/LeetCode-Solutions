class Solution:
    def reverseWords(self, s: str) -> str:
        # remove trailing and leading spaces and convert to list of strings
        words = s.strip().split()
        left, right = 0, len(words)-1
        # swap the data
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        # join back to strings
        return ' '.join(words)