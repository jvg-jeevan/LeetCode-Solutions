class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        for i in range(101):
            if ((i + 1) * k) not in nums:
                return (i + 1) * k
        