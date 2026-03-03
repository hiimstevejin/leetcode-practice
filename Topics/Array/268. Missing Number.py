class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            val = nums[i]
            # If the number is within bounds and not in its correct place
            if val < n and nums[i] != nums[val]:
                nums[i], nums[val] = nums[val], nums[i] # Swap
            else:
                i += 1 # Only move forward when current index is 'resolved'

        # Final check: which index doesn't match its value?
        for i in range(n):
            if nums[i] != i:
                return i
        return n


        # n = len(nums)
        # Tsum = (n * (n +1)) // 2
        # actual_sum = sum(nums)
        # return Tsum - actual_sum
