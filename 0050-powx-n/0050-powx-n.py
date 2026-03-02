class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if odd x*x^(n-1) = x^n
        # if even x^n = (x^(n/2))^2
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n > 0:
            if n%2 != 0:
                res *= x
            x = x*x
            n //= 2
        return res