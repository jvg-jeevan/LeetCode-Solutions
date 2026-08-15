class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        full_res = 0


# get the xor of all the elements if all xor non zero then return same array length

# check if every element is non zero if not then return 0 

# if xor is zero then xor with one elemnent less will result in the number same as the excluded number as x^0 = x and x^x = 0
        non_zero = False
        for i in nums:
            full_res ^= i
            if i != 0:
                non_zero = True 


        if full_res != 0:
            return len(nums)
        elif non_zero == False:
            return 0
        else:
            return len(nums)-1
        