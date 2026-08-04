class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(min(nums), max(nums)+1):
            if i not in nums:
                res.append(i)

        return res