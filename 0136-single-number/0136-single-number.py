class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res

        # xor of same number results in 0
        # so the same numbers gets of cancelled