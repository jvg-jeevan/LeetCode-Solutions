class Solution:
    def intToRoman(self, num: int) -> str:

# creating the maps for numbers and corressponding symbols
        values = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]

        symbols = [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
        ]

        res = []
# iterate simultaneously
        for val, sym in zip(values, symbols):
# if the num is greater than the current value taken then sub that value and add the corressponding symbol to res
            while num >= val:
                res.append(sym)
                num -= val

        return ''.join(res)