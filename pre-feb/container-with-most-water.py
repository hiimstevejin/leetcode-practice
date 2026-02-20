class Solution:
	def maxArea(self, heights: list[int]) -> int:
		l,r = 0, len(heights) -1
		area = 0
		while l < r:
			area = max(area, min(heights[l], heights[r]) * (r-l))
			if (heights[r] > heights[l]):
				l += 1
			else:
				r -= 1
		return area

solution = Solution()
ex = [1,7,2,5,4,7,3,6]
print(solution.maxArea(ex))
ex2 = [2,2,2]
print(solution.maxArea(ex2))
