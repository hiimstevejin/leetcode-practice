from collections import defaultdict

class Solution:
	def isAnagram(self, s: str, t:str) -> bool:
		if (len(s) != len(t)):
			return False

		d = defaultdict(int)

		for c in range(len(s)):
			d[c] += 1
		
		for c in range(len(t)):
			if d[c] == 0:
				return False
	
			d[c] -= 1

		return True

s1 = "abcdefg"
s2 = "gfedcba"

solution = Solution()
print(solution.isAnagram(s1,s2))
