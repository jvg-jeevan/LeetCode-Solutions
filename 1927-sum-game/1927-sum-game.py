class Solution:
    def sumGame(self, nums: str) -> bool:
        left_sum = 0
        right_sum = 0
        q_left = 0
        q_right = 0

        half = len(nums) // 2

        for i in range(half):
            if nums[i] == '?':
                q_left += 1
            else:
                left_sum += int(nums[i])
            
            if nums[i + half] == '?':
                q_right += 1
            else:
                right_sum += int(nums[i + half])

        # return (2 * abs(left_sum - right_sum)) != (9 * abs(q_left - q_right))
        return 2 * (left_sum - right_sum) != 9 * (q_right - q_left)