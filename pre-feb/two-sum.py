class Solution:
	def twoSum(self, nums: list[int], target: int)-> list[int]:
		d ={}
		for i in range(len(nums)):
			diff = target - nums[i]
			if diff in d:
				return [d[diff], i]
			d[nums[i]] = i

solution = Solution()
arr = [1,2,3,4,5]
target = 9
print(solution.twoSum(arr,target))
