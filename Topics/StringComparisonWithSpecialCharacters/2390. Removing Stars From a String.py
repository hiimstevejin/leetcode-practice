class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c == "*":
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
    def removeStars(self, s: str) -> str:
        stk = []
        res = []
        for i in range(len(s)-1,-1,-1):
            stk.append(s[i])
        while stk:
            curr = stk.pop()
            if curr == "*":
                res.pop()
            else:
                res.append(curr)
        return "".join(res)
