class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count to track the number of times
        count = 0
        # candidate to track the num
        candidate = None
        for num in nums:
            # if count is 0 then assign the candidate with num
            if count == 0:
                candidate = num
            # else increment count if current num = candidate else assign -1
            count += 1 if num == candidate else -1
        return candidate