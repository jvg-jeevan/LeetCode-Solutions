class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def getSum(val):
            res = 0
            while val > 0:
                res += val % 10
                val //= 10
            return res
            
        num = 0
        for i in s:
            num += getSum(ord(i) - ord('a') + 1)

        while k > 1:
            num = getSum(num)
            k -= 1

        return num        