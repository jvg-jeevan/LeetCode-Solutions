class Solution:
    def check(self, nums: List[int]) -> bool:
        # for rotated ones only 1 time break from increasing order like 5 -> 1
        # check if break present that too <= 1
        # compare i > (i+1) mod (len(nums)) i.e current and next element and for last element it will be last and first element comparison

        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                res += 1
        
        return res <= 1