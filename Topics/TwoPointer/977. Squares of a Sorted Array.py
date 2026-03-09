class Solution:
    # O(N) with O(N) space
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        i = len(nums) - 1

        while l <= r:
            sqrtl = nums[l] * nums[l]
            sqrtr = nums[r] * nums[r]
            if sqrtl <= sqrtr:
                res[i] = sqrtr
                r -= 1
            else:
                res[i] = sqrtl
                l += 1
            i -= 1

        return res
