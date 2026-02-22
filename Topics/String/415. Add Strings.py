# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        zero = ord("0")
        p1 = len(num1) -1
        p2 = len(num2) -1
        carry = 0

        while p1 >= 0 or p2 >= 0 or carry:
            digit1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            digit2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            res += chr(total % 10 + ord('0'))


            p1 -=1
            p2 -=1

        return res[::-1]
