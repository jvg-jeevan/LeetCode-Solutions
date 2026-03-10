class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        min_sum = cur_min = nums[0]
        for i in range(1, n):
            cur_min = min(nums[i], nums[i] + cur_min)
            min_sum = min(min_sum, cur_min)
        
        max_sum = cur_max = nums[0]
        for i in range(1, n):
            cur_max = max(nums[i], nums[i] + cur_max)
            max_sum = max(max_sum, cur_max)

        if max_sum < 0:
            return max_sum
        
        total = sum(nums)
        return max(max_sum, total - min_sum)