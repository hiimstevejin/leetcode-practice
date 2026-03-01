# O(N) Solution with O(1) Space
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.max_count = 0
        self.current_count = 0
        self.prev_val = None
        self.res = []

        def in_order(node):
            if not node:
                return

            # Traverse Left
            in_order(node.left)

            # Process Current Node (The "Sorted" logic)
            if node.val == self.prev_val:
                self.current_count += 1
            else:
                self.current_count = 1

            # Update Result
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.res = [node.val]
            elif self.current_count == self.max_count:
                self.res.append(node.val)

            self.prev_val = node.val

            # Traverse Right
            in_order(node.right)

        in_order(root)
        return self.res
