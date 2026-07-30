class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # to track numbers
        dp = {}
        res = 1
        for num in arr:
            # to check if the difference - number exists in the arr if exists then increment that value by 1
            prev = num - difference
            # in get if default 0 not specified raises error
            dp[num] = dp.get(prev, 0) + 1
            res = max(dp[num], res)
        return res