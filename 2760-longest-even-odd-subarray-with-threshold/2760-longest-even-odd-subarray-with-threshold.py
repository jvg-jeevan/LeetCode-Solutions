class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        cur = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                cur = 0
                
            elif cur == 0:
                if nums[i] % 2 == 0:
                    cur = 1
            else:
                if nums[i] % 2 != nums[i-1] % 2:
                    cur += 1
                else:
                    if nums[i] % 2 == 0:
                        cur = 1
                    else:
                        cur = 0
            res = max(res, cur)

        return res