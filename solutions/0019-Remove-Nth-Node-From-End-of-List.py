# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        length = getLength(head)
        dummy = ListNode(0,head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur  = cur.next
        cur.next = cur.next.next
        return dummy.next 
