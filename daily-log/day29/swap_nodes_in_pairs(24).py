# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        while curr and curr.next:
            next_pair = curr.next.next
            tmp = curr.next
            tmp.next = curr
            curr.next = next_pair
            prev.next = tmp
            prev = curr
            curr = next_pair

        return dummy.next
        
