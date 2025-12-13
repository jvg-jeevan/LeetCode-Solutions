class Solution:
    def secondHighest(self, s: str) -> int:
        nums = [int(i) for i in s if i.isnumeric()]
        gold = silver = -1

        # similar to race 
        # 1 -> gold, 2 -> silver
        # if one overtakes silver he will be in silver
        # if one overtakes gold then he will get gold and current gold gets silver
        for num in nums:
            if num > gold:
                silver = gold
                gold = num
            elif silver < num < gold:
                silver = num
        return silver