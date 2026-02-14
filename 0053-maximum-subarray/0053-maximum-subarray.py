class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # take 1st element as sums
        cur_sum = nums[0]
        max_sum = nums[0]
        # add each element to cur sum and check if element is larger than the cur_sum + element
        # store max of the cur sum and max sum
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        
        return max_sum