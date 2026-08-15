class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            # next to current element index
            left = i + 1
            # last element index
            right = len(nums) - 1

            while left < right:
                # to get to the closest sum possible
                cur_sum = nums[i] + nums[left] + nums[right]
                
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                
                # as sorted moving left to next element gets higher value
                if cur_sum < target:
                    left += 1
                # as sorted moving left to next element gets lower value                
                elif cur_sum > target:
                    right -= 1
                
                else:
                    return target
        
        return closest 