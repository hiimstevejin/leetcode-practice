class Solution:
    def maxArea(self, height: List[int]) -> int:
        # calculate area inside of two pointers and move the smaller point inward at each step
        max_area = 0
        l = 0
        r = len(height)-1

        while l < r:
            w = r - l
            h = min(height[r],height[l])
            max_area = max(max_area, w * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
