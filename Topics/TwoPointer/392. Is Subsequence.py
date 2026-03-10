class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_indices = defaultdict(list)
        for i, char in enumerate(t):
            char_indices[char].append(i)

        # For each 's', use Binary Search to find the next valid index
        current_pos = -1
        for char in s:
            if char not in char_indices: return False
            # Find the smallest index > current_pos
            indices = char_indices[char]
            idx_in_list = bisect.bisect_right(indices, current_pos)
            if idx_in_list == len(indices): return False
            current_pos = indices[idx_in_list]
    # Two-pointer approach O(N) Time
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0
        if not s:
            return True
        while pt < len(t):
            if t[pt] == s[ps]:
                ps += 1
                if ps == len(s):
                    return True
            pt += 1
        return False
