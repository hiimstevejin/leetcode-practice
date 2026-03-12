class Solution:
    # Time Complexity: O(n) Space Complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        l = 0
        for r in range(1,len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r],nums[l]
                l+= 1
        return l
