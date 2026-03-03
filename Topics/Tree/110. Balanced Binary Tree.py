# If brute forced it would be O(N^2) times because depth is calculated at each node for every node
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This solution more intuitive in my opinion
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) > 1:
                self.res = False

            return max(left,right) + 1

        dfs(root)
        return self.res

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            balanced = (left[0] and right[0] and abs(left[1]-right[1])< 2)
            return [balanced, 1+ max(left[1],right[1])]

        return dfs(root)[0]
