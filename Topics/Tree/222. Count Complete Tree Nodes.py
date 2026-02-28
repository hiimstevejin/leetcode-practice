# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(Log ^ 2 (N))
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_level = 1
        l = root.left
        while l:
            l = l.left
            left_level += 1

        right_level = 1
        r = root.right
        while r:
            r = r.right
            right_level += 1

        if right_level == left_level:
            return (2 ** left_level)-1

        return 1+ self.countNodes(root.left) + self.countNodes(root.right)


        # BELOW ARE O(N) Approaches
        # def dfs(node):
        #     if not node:
        #         return 0

        #     return 1 + dfs(node.left) + dfs(node.right)
        # return dfs(root)


        # if not root:
        #     return 0
        # q = deque([root])
        # res = 0
        # while q:
        #     length = len(q)
        #     res += length
        #     for i in range(length):
        #         curr = q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)

        # return res
