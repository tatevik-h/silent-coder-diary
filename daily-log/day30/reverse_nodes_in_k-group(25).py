# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        count = 0

        while node and count < k:
            node = node.next
            count += 1

        if count < k:
            return head

        prev = None
        curr = head
        next_node = None
        count = 0

        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        if next_node:
            head.next = self.reverseKGroup(next_node, k)

        return prev
        
