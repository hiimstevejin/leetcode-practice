# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            depth += 1
        return depth

        # if not root:
        #     return 0

        # # If one child is None, we must traverse the other path
        # if not root.left: return self.minDepth(root.right) + 1
        # if not root.right: return self.minDepth(root.left) + 1

        # # If both children exist, take the minimum
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
