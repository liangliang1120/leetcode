# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
         #  to avoid category discussions
        dummy = ListNode(-1)
        dummy.next = head
        # get the left boundary, left start node
        # get the right boundary, right start node
        i = 1
        left_b = dummy
        x = 1
        right_dummy = head
        while i < left:
            i += 1
            left_b = left_b.next
        while x < right :
            x += 1
            right_dummy = right_dummy.next
        left_dummy = left_b.next
        right_b = right_dummy.next
        # cut off right dummy to right boundary
        right_dummy.next = None
        
        # end with right_b
        cur = right_b
        pre = left_dummy
        while pre:
            temp = pre.next
            pre.next = cur
            cur = pre
            pre = temp
        left_b.next = cur
        return dummy.next

