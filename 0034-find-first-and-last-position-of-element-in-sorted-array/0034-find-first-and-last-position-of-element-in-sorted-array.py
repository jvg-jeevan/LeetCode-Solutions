class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def searchOccurrence(nums, target, isfirst):
            res = -1
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low+high)//2
                if target < nums[mid]:
                    high = mid-1
                elif target > nums[mid]:
                    low = mid+1
                else:
                    res = mid
                    if isfirst:
                        high = mid-1
                    else:
                        low = mid+1
            return res    

        return [searchOccurrence(nums, target, True), searchOccurrence(nums, target, False)]