class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # mountain and peak
        # if current < next peak to right
        # else peak to left
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return low