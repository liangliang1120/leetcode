# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        tmp = 0
        while l1 or l2 or tmp > 0:
            if l1 and l2:
                if l1.val + l2.val + tmp < 10:
                    new_node = ListNode(l1.val + l2.val + tmp )
                    tmp = 0
                else:
                    new_node = ListNode(l1.val + l2.val + tmp  - 10)
                    tmp = 1
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if l1.val + tmp < 10:
                    new_node = ListNode(l1.val + tmp )
                    tmp = 0
                else:
                    new_node = ListNode(l1.val + tmp - 10)
                    tmp = 1
                l1 = l1.next
            elif l2:
                if l2.val + tmp < 10:
                    new_node = ListNode(l2.val + tmp )
                    tmp = 0
                else:
                    new_node = ListNode(l2.val + tmp - 10)
                    tmp = 1
                l2 = l2.next
            else:
                new_node = ListNode(tmp)
                tmp = 0
            cur.next = new_node
            cur = cur.next
            
        return dummy.next
