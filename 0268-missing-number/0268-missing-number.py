class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # expected = (n * (n+1)) // 2
        # return expected - sum(nums)

        # a ^ a = 0 a ^ 0 = a
        # xor all indices and all integers in nums results in missing number

        xor = 0
        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]

        xor ^= len(nums)
        return xor