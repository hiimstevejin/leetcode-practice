class Solution:
    # Time O(N) # Space O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window = len(nums) + 1
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                window = min(window, r-l+1)
                curr_sum -= nums[l]
                l += 1

        if window > len(nums):
            return 0
        return window
