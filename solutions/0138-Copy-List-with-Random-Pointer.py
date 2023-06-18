"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p = head
        # 1.copy node # 1->1'->2->2'->3->3'
        while p:
            new_node = Node(p.val, None, None) # copy value 1'
            new_node.next = p.next # 1'->2
            p.next = new_node # 1 -> 1'
            p = new_node.next # p from 1 to 2

        # 2.copy random for 1', 2'
        p = head
        while p:
            if p.random:
                # random.next is copied newnode with same value
                p.next.random = p.random.next
            p = p.next.next

        # split two linkedlist
        dummy = Node(-1)
        p = head # start from head
        cur = dummy # start from -1
        while p:
            cur.next = p.next
            cur = p.next
            p = p.next.next

        return dummy.next



