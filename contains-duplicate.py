class Solution:
	def hasDuplicate(self, nums: list[int]) -> bool:
		s = set()
		for num in nums:
			if num in s:
				return True
			s.add(num)
		return False

ex_1 = [1,2,3,4,1]
ex_2 = [1,1,2]
ex_3 = [1,2,3,4]
problem_set = [ex_1, ex_2, ex_3]

solution = Solution()

for ex in problem_set:
	print(ex)
	print(solution.hasDuplicate(ex))
