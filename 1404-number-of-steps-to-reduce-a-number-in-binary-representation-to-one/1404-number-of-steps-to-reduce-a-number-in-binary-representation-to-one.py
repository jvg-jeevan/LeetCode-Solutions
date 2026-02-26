class Solution:
    def numSteps(self, s: str) -> int:
        if s == '1':
            return 0

        num = 0
        n = len(s)-1
        for i in range(n, -1, -1):
            num += ((ord(s[n-i]) - 48) * (2**i))
        
        count = 0
        while num != 1:
            if num % 2 != 0:
                num += 1
            else:
                num //= 2
            count += 1
        return count