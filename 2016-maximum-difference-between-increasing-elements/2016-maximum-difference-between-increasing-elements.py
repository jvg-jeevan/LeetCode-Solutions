class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        res = -1
        for num in nums[1:]:
            if num > min_val:
                res = max(res, num - min_val)
            else:
                min_val = num
            
        return res