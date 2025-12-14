class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # start = 0 
        # end = len(s) - 1
        # while start < end:
        #     s[start], s[end] = s[end], s[start]
        #     start += 1
        #     end -= 1

        half = len(s) // 2
        for i in range(1, half+1):
            s[i-1], s[-i] = s[-i], s[i-1]
        