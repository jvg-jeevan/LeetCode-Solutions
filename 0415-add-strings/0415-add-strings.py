class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # base case
        if num1 == '0' and num2 == '0':
            return '0'


        num = self.str_to_int(num1) + self.str_to_int(num2)
        res = []
        # converting num to string
        while num > 0:
            res.insert(0, chr((num%10) + 48))
            num //= 10
        return ''.join(res)

    # string to integer
    def str_to_int(self, n):
        num = 0
        for i in n:
            num = (num * 10) + (ord(i) - 48)
        return num