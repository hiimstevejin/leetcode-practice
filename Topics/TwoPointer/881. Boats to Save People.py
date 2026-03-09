class Solution:
    # O(NlogN)
    # fat person goes on always and try to shove remaining space with another skinny person
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        l = 0
        r = len(people) - 1
        while l <= r:
            curr_weight = people[l] + people[r]
            if curr_weight <= limit:
                l += 1
            res += 1
            r -= 1
        return res
