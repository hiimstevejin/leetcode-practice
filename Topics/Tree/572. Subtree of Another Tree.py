# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# O(N^2) Time Complexity
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(r, s):
            if not r and not s:
                return True

            if r and s and r.val == s.val:
                return same(r.right, s.right) and same(r.left, s.left)
            return False

        if not subRoot:
            return True

        if not root:
            return False

        if same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
