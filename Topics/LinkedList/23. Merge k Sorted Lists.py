import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        count = 0
        for head in lists:
            while head:
                heapq.heappush(pq, (head.val,count, head))
                count += 1
                head = head.next
        dummy = ListNode()
        node = dummy

        while pq:
            cur_node = heapq.heappop(pq)[2]
            node.next = cur_node
            node = node.next
        return dummy.next
