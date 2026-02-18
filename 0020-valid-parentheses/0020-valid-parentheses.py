class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        stack = []
        smap = {
            ')': '(', 
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in smap.values():
                stack.append(i)
            else:
                if not stack or stack[-1]  != smap[i]:
                    return False
                stack.pop()

        return len(stack) == 0