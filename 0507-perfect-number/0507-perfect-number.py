class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 1
        i = 2
        # get divisors until sqrt(n) in terms of pairs (x, y)
        while i*i <= num:
            if num%i == 0:
                sum += i
                # if x divides num then y should also divide num
                # inequality check to avoid duplicating values
                if i != num//i:
                    sum += (num//i)
            i += 1

        print(sum)
        return sum == num