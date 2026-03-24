class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = [0] * 26
        max_freq = 0
        l = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, freq[ord(s[r])-ord('A')])
            while r-l+1 - max_freq > k:
                freq[ord(s[l])-ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
