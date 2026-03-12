class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        # d = defaultdict(int)
        # for num in nums:
        #     d[num] += 1

        # idx = 0

        # for color in range(3):
        #     freq = d[color]
        #     nums[idx: idx + freq] = [color] * freq
        #     idx += freq
