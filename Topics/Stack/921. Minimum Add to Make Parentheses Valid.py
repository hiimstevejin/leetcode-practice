# Example 1:

# Input: s = "())"
# Output: 1
#
# O(N) Time & O(N) Space
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for i in range(len(s)):
            if not stk:
                stk.append(s[i])

            else:
                if stk[-1] == "(" and s[i] == ")":
                    stk.pop()
                else:
                    stk.append(s[i])

        return len(stk)

# O(N) Time & O(1) Space
class Soltion:
    def minAddToMakeValid(self, S):
        left = right = 0
        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left + right
