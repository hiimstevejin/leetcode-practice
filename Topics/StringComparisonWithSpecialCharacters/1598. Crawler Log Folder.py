class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minOperations(self, logs: List[str]) -> int:
        layer = 0
        for log in logs:
            if log == "../":
                if layer > 0:
                    layer -= 1
            elif log != "./":
                layer += 1
        return layer
