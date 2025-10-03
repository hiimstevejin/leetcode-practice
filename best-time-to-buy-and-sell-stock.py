class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		l,r = 0, 1
		max_profit = 0

		while r < len(prices):
			if prices[l] < prices[r]:
				profit = prices[r] - prices[l]
				max_profit = max(max_profit, profit)
			else:
				l = r
			r += 1 
		return max_profit

solution = Solution()
ex = [7,4,1,5,7,2,10]
print(solution.maxProfit(ex))
