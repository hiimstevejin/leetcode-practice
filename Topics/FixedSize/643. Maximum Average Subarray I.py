class Solution:
    # Time: O(n), Space: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        total = 0
        for i in range(k):
            total += nums[i]
        res = total
        for r in range(k, len(nums)):
            total += nums[r]
            total -= nums[l]
            res = max(res,total)
            l += 1
        return res/k
