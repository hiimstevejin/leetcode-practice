class Solution:
    # Time O(N)
    # Space O(1)
    # Both same two pointer approach
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r = len(s) -1
        for l in range(len(s)):
            if not r > l:
                break
            s[l], s[r] = s[r], s[l]
            r -= 1
