# O(N) Time, O(H) Space
# Doing Inorder Traversal returns node in the sorted order so we can compare the values to find the minimum absolute difference.

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev = None  # Tracks the previously visited node in-order

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff
