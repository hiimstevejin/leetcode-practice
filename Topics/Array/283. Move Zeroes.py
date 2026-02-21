# two pointer method
# when right pointer finds the first non-zero element, swap it with the element at the left pointer and increment left pointer
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
