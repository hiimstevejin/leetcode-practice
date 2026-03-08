class Solution:
    # Two pointer approach O(N) Time O(1) Space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Problem asks for 1-based indexing
                return [left + 1, right + 1]

            if current_sum > target:
                right -= 1
            else:
                left += 1

    # HASHMAP Approach O(N) Time O(N) Space
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     # 1<= i_1 < i<2 <= len(nums)
    #     # return i_1 and i_2 incremented by one as [i_1, i_2]
    #     d = {}
    #     for j in range(len(numbers)):
    #         d[target-numbers[j]] = (j)

    #     for i in range(len(numbers)):
    #         if numbers[i] in d and d[numbers[i]] != i:
    #             return [i+1, d[numbers[i]]+1]
