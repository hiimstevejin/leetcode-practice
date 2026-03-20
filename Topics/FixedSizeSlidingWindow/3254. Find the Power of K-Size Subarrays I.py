class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k == 1:
            return nums

        good = 0
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                good += 1

        res = []
        if good == k - 1:
            res.append(nums[k - 1])
        else:
            res.append(-1)

        for r in range(k, n):
            # remove left adjacent pair from previous window
            if nums[r - k + 1] == nums[r - k] + 1:
                good -= 1

            # add new right adjacent pair
            if nums[r] == nums[r - 1] + 1:
                good += 1

            if good == k - 1:
                res.append(nums[r])
            else:
                res.append(-1)

        return res
