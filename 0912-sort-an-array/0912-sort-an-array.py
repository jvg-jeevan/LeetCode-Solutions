class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # using mergesort

        def mergeSort(low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSort(low, mid)
            mergeSort(mid+1, high)
            merge(low, mid, high)


        def merge(low, mid, high):
            i, j, k = 0, 0, low
            left = nums[low: mid+1]
            right = nums[mid+1: high+1]

            while i<len(left) and j<len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    k += 1
                    i += 1
                else:
                    nums[k] = right[j]
                    k += 1
                    j += 1
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1
            return nums

        mergeSort(0, len(nums)-1)
        
        return nums