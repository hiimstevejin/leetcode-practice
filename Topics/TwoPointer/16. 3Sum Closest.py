class Solution:
    # O(N^2) time and O(1) Space
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # values with distinc indicies closest to target
        diff = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                curr_diff = abs(total-target)
                if curr_diff < diff:
                        diff = curr_diff
                        res = total
                if total > target:
                    k-=1
                if total < target:
                    j+=1



        return res
