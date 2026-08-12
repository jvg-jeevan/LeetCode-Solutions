class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        res = 0

        for right in range(len(nums)):
            # to track freq
            # get to ensure that it doesnot raise any errors
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # if the freq is higher than k then reduce the freq using left and increment left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res