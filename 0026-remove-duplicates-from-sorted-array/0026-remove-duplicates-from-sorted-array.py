class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use two pointer one to read and other to write
        # in read if previous element same as current then skip
        # if not then place the current read in the write position and update write
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write