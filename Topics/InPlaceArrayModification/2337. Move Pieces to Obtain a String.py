class Solution:
    # Time O(N)
    # Space O(1)
    # check if the sequences of L and R are the same and the positions are valid
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        p1 = 0
        p2 = 0
        n = len(start)

        while p1 < n or p2 < n:
            while p1 < n and start[p1] == "_":
                p1 += 1
            while p2 < n and target[p2] == "_":
                p2 += 1

            if p1 == n and p2 == n:
                return True
            if p1 == n or p2 == n:
                return False

            if start[p1] == "L" and p1 < p2:
                return False
            if start[p1] == "R" and p1 > p2:
                return False

            p1 += 1
            p2 += 1

        return True

class Solution:
    # My solution that is dirty kinda
    def canChange(self, start: str, target: str) -> bool:
        sequence = ""
        end_sequence = ""
        for s in start:
            if s != "_":
                sequence += s
        for e in target:
            if e != "_":
                end_sequence += e
        if sequence != end_sequence:
            return False
        if "L" not in sequence and "R" not in sequence:
            return True
        p1 = 0
        p2 = 0
        while p1 < len(start) and p2 < len(target):
            while p1 < len(start) and start[p1] == "_":
                p1 += 1
            while p2 < len(target) and target[p2] == "_":
                p2 += 1
            if p1 == len(start) and p2 == len(target):
                return True
            if p1 == len(start) or p2 == len(target):
                return False
            curr_start = start[p1]
            if curr_start == "L":
                if p1 < p2:
                    return False
            elif curr_start == "R":
                if p1 > p2:
                    return False
            p1 += 1
            p2 += 1
        return True
