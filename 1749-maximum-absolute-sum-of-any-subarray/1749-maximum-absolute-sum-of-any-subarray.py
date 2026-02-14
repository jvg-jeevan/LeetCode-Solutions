class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_1, max_sum = 0, 0
        min_1, min_sum = 0, 0

        for num in nums:
            max_1 = max(num, num + max_1)
            max_sum = max(max_sum, max_1)

            min_1 = min(num, num + min_1)
            min_sum = min(min_1, min_sum)

        return max(abs(min_sum), abs(max_sum))