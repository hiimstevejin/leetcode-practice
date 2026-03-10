class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def isHappy(self, n: int) -> bool:
        def get_next_number(num):
            output = 0
            while num:
                digit = num % 10
                output += digit ** 2
                num //= 10
            return output

        slow = get_next_number(n)
        fast = get_next_number(slow)
        while slow != fast:
            if fast == 1:
                return True
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))
        return slow == 1
