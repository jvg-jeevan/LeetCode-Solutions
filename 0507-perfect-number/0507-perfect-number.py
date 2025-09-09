class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 1
        i = 2
        # get divisors until sqrt(n)
        while i*i <= num:
            if num%i == 0:
                sum += i
                if i != num//i:
                    sum += (num//i)
            i += 1

        # # finding divisor from sqrt(n) to n excluded
        # while i>1:
        #     if num%i == 0:
        #         sum += (num//i)
        #     i -= 1
        print(sum)
        return sum == num