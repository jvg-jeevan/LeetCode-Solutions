class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # res to store all the triples
        res = []
        # checking whether the next 3 are tiples if there add to res
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                res.append(num[i] + num[i+1] + num[i+2])
        # return the highest value
        return max(res) if res else ''