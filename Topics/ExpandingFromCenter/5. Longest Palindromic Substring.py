class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return s[l+1:r]
                l -= 1
                r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            even_palindrome = expand(i-1,i)
            odd_palindrome = expand(i,i)
            if len(even_palindrome) > len(res):
                res = even_palindrome
            if len(odd_palindrome) > len(res):
                res = odd_palindrome
        return res
