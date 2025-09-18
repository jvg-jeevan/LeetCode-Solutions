class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'


        num1 = self.get_int(num1)
        num2 = self.get_int(num2)
        res = num1 * num2
        ans = ''
        # converting int to str 
        while res > 0:
            ans += chr((res%10) + 48)
            res //= 10
        # returnt the reverse of str as it adds to end of the string
        return ans[::-1]


    # converting into integer using ascii value
    def get_int(self, n):
        num = 0
        for i in n:
            num = (ord(i) - 48) + (num * 10) 
        return num