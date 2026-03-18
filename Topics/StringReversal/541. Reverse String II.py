class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def reverseStr(self, s: str, k: int) -> str:
        res = [char for char in s]
        for start in range(0,len(s),2*k):
            left = start
            right = min(start+k-1, len(s)-1)

            while left < right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
        return "".join(res)
