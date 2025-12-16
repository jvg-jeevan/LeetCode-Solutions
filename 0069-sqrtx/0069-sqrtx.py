class Solution:
    def mySqrt(self, x: int) -> int:
        # same way as binary search
        # take the mid and see if perfect square if not continue
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif x < mid*mid:
                high = mid-1
            else:
                low = mid+1
        # when low>high return high because it is the closest sqrt as low is already reached higher
        return high