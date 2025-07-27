# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def partone(head):
            if not head:
                return None, None
            
            left, right = partone(head.next)

            if head.val < x:
                head.next = left
                return head, right
            else:
                head.next = right
                return left, head

        left , right = partone(head)

        if not left:
            return right
            
        curr = left
        while curr.next:
            curr = curr.next
        curr.next = right

        return left
      
## Iterativ approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None

        return left.next
