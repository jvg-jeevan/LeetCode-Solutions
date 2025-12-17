class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid+1] < nums[mid]:
                low = mid+1
            else:
                high = mid
        return nums[low]