class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def lomuto_partition(nums, low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i+1

        def quicksort(nums, low, high):
            if low <= high:
                index = lomuto_partition(nums, low, high)
                quicksort(nums, low, index-1)
                quicksort(nums, index+1, high)
        
        quicksort(nums, 0, len(nums)-1)

        # using insertion sort
        # for i in range(1, len(nums)):
        #     key = nums[i]
        #     j = i-1
        #     while j>=0 and nums[j]>key:
        #         nums[j+1] = nums[j]
        #         j -= 1
        #     nums[j+1] = key