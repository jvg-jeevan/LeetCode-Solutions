class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        i = 0
        ans = 0
        while n != 0:
            if n % 2 == 0:
                ans += (1 * (2**i))
            i += 1
            n //= 2
        return ans