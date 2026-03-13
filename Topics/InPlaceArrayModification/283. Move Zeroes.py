class Solution:
    # put elements equal to zero at r pointer
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(1,len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[r],nums[l] = nums[l], nums[r]
                l += 1
            if nums[l] != 0:
                l += 1
    #
    # Two pointer
    # Time O(n)
    # Space O(1)
    # put in none-zero elements at the l pointer.
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
