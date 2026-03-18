class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        arr = list(s)

        l, r = 0, len(arr) - 1

        while l < r:
            while l < r and arr[l] not in vowels:
                l += 1
            while l < r and arr[r] not in vowels:
                r -= 1

            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return "".join(arr)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        left = 0
        right = len(s) - 1
        arr = [char for char in s]
        while left < right:
            while s[left].lower() not in vowels and left < right:
                left += 1
            while s[right].lower() not in vowels and left < right:
                right -= 1

            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return "".join(arr)
