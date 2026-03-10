class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         Phase 1 (Cycle Detection):
# Move the tortoise and hare, advancing the hare twice as fast as the tortoise, until the hare catches up with the tortoise or a cycle is detected. If a cycle is detected, reset the tortoise and move the hare back to its position before the reset.

# Phase 2 (Cycle Start Detection):
# Move the tortoise and hare one step at a time until they match again. The position where they match again is the starting point of the cycle, corresponding to the duplicate element.
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the duplicate (entrance to cycle)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
