class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l, r = 0, len(words) - 1

        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1

        return " ".join(words)
    # Time Complexity: O(n^2) because string concatenation is O(n) and we do it n times
    # everytime you do res += curr, you are creating a new string, which is O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.strip()
        stk = []
        p  = len(s) - 1
        while p >= 0:
            if s[p] != " ":
                stk.append(s[p])
                p -= 1
            elif s[p] == " ":
                while stk:
                    curr = stk.pop()
                    res += curr
                while s[p] == " ":
                    p -= 1
                res += " "
        while stk:
            res += stk.pop()
        return res
