from typing import Optional

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        My solution O(N) time no value assigning O(1) Space
        """
        if not head or not head.next:
            return head

        dummy = ListNode(val = 0, next=head)
        first = head
        second = head.next
        prev = dummy

        while second:
            next_first = first.next.next
            next_second = second.next.next if second.next and second.next.next else None
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
            first = next_first
            second = next_second

        return dummy.next

    def swapPairsOptimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal solution O(N) time no value assigning O(1) Space
        """
        # Handle base cases
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Ensure there is a pair (two nodes) to swap
        while prev.next and prev.next.next:
            # Identify the nodes in the pair
            first = prev.next
            second = prev.next.next

            # THE SWAP:
            # 1. Point first to the node AFTER the pair
            first.next = second.next
            # 2. Point second back to first
            second.next = first
            # 3. Connect the previous part of the list to second
            prev.next = second

            # Move prev two steps forward for the next pair
            prev = first

        return dummy.next
