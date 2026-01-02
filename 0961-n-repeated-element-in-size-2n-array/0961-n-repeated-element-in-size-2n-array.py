class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        res = {}
        for i in set(nums):
            res[i] = nums.count(i)

        n = len(nums)//2

        for i, c in res.items():
            if c == n:
                return i