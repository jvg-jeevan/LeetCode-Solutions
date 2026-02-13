class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # track ones with res and store the max value of res in max_res
        res = 0
        max_res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                res += 1
                max_res = max(res, max_res)
            else:
                res = 0
        return max_res