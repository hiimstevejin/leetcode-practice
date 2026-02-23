# binary search in sorted part of the array
# return immediately if the middle element is the target
# else, compare left and mid -> if left <= mid this means that the left part is sorted
#   1. if looking into this sorted part, the condition nums[left] <= target < nums[mid] is met (which means that this part of array is sorted and target is inside of this part), set right = mid - 1
#   2. else, search the other part of the arr which is not sorted but in the next iteration, we will find the sorted part of this arr
#   if condition 1 is false, then search the other part of the array and see if target is between nums[mid] and nums[right] if this condition is met, we search the right part of the array because it means the right part of this unsorted array is sorted and target is inside of this part
#   else we search the left half of this array
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
