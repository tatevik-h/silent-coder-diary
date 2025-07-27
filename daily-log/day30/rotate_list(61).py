# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateOnce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        while curr.next:
            prev = curr
            curr = curr.next

        prev.next = None
        curr.next = head
    
        return curr

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        def get_length(node):
            if not node:
                return 0
            return 1 + get_length(node.next)

        length = get_length(head)
        if k % length == 0:
            return head

        return self.rotateRight(self.rotateOnce(head), k-1)
      
