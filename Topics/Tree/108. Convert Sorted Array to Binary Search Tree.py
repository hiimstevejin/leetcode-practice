# interesting solution involving two pointer and recursion
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) -1
        def createTree(nums, start, end):
            if start > end:
                return
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = createTree(nums, start, mid-1)
            node.right = createTree(nums, mid+1, end)
            return node
        return createTree(nums, start, end)
