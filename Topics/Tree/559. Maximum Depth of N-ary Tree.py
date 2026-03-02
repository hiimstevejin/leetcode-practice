"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    # Recursive DFS O(N) Time Complexity,  O(H) Space Complexity
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        if not root.children:
            return 1

        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))

        return 1 + max_depth

    # Bredth First Search O(N) Time Complexity, O(W) Space Complexity
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque([root])
        res = 0

        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                if not curr:
                    continue
                for child in curr.children:
                    q.append(child)

            res += 1

        return res
