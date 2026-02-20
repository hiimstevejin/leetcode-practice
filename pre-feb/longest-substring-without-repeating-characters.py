class Solution:
	def lengthOfLongestSubstring(self, s:str) -> int:
		# first initialize set, left, window, res
		char_set = set()
		left = 0
		window = 0
		res = 0

		for right in range(len(s)):
			while s[right] in char_set:
				char_set.remove(s[left])
				left += 1
				window -= 1
			window += 1
			char_set.add(s[right])
			res = max(window, res)

		return res

solution = Solution()
ex = "abaabdedabcd"
print(solution.lengthOfLongestSubstring(ex))
