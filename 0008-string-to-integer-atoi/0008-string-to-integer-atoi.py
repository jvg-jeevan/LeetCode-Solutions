class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        s = s.strip()

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]

        for i in s:
            if ord(i) >= 48 and ord(i) <= 57:
                res =  (res * 10)+ ord(i)-48
            else:
                break
        return sign * res