class Solution:
    # Time Complexity: O(n) Space Complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = 1
        for r in range(len(nums)):
            if nums[r] != nums[l-1]:
                nums[l] = nums[r]
                l += 1
        return l
