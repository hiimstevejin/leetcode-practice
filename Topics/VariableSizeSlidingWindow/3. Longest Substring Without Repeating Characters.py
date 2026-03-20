class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep char in window with set
        # sliding window
        # in every iteration of loop check if s[r] in seen
        # if in, shrink until s[r] not in window anymore by removing s[l]
        # Time O(N) # Space O(N)
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r-l+1)
        return res
