from typing import Optional

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the nth node from the end of list. How?
        # 1. could number nodes as we go and traverse again. Until we reach that number from the end and remove it
        # 1 means end of list
        # if not head:
        #     return head

        # node = head
        # length = 0
        # while node:
        #     length += 1
        #     node = node.next

        # dummy_node = ListNode()
        # dummy_node.next = head

        # target = length - n + 1
        # prev = dummy_node
        # curr = 1
        # while head:
        #     if curr == target:
        #         prev.next = head.next
        #         break
        #     curr += 1
        #     prev = head
        #     head=head.next


        # return dummy_node.next

        # 2. one pass use fast slow pointer
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head
        # dum -> 1 -> 2 -> 3 -> 4 -> (5) -> 6 -> 7 -> 8
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
