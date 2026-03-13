class Solution:
  # O(N) time O(N) Space
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
    # O(N) time O(1) Space better approach
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        while l < r:
            while nums[l] % 2 == 0 and l <r:
                l += 1
            while nums[r] % 2 == 1 and l < r:
                r -= 1
            nums[l], nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        return nums
