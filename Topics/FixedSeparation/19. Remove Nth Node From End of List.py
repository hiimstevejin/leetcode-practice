# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(n) Space: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        nth = dummy
        for _ in range(n):
            nth = nth.next
        while nth.next:
            node = node.next
            nth = nth.next
        node.next = node.next.next

        return dummy.next
