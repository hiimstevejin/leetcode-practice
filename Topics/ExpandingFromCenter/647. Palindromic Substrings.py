class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        def expand(l,r,s):
            length = len(s)
            count = 0
            while l >=0 and r < length:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            return count

        res = 0
        length = len(s)
        for i in range(length):
            res += expand(i-1,i,s)
            res += expand(i,i,s)
        return res
