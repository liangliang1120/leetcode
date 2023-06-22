### [206. Reverse Linked List](https://github.com/liangliang1120/leetcode/blob/main/solutions/0206-Reverse-Linked-List.py)
- pre = head, cur = None
- Time: O(n), Space: O(1) iteration


### [92. Reverse Linked List II](https://github.com/liangliang1120/leetcode/blob/main/solutions/0092-Reverse-Linked-List-II.py)
- Time: O(n), Space: O(1) iteration

### [21. Merge Two Sorted Lists](https://github.com/liangliang1120/leetcode/blob/main/solutions/0021-Merge-Two-Sorted-Lists.py)
- dummy = ListNode(-1), temp = dummy
- temp.next = l1 if l1 is not None else l2
- Time: O(n+m), Space: O(1) iteration

### [143. Reorder List](https://github.com/liangliang1120/leetcode/blob/main/solutions/0143-Reorder-List.py)
- if use list to record all, Time: O(n), Space: O(n)
- find the mid point of the linkedlist, reverse the order of the second half, merge 2 linkedlist
- Time: O(n), Space: O(1)

### [19. Remove Nth Node From End of List](https://github.com/liangliang1120/leetcode/blob/main/solutions/0019-Remove-Nth-Node-From-End-of-List.py)
-  get the length of the linkedlist
-  have a dummy from the pre-node of head, because the first node might be deleted
-  Time: O(n), Space: O(1)

### [138. Copy List with Random Pointer](https://github.com/liangliang1120/leetcode/blob/main/solutions/0138-Copy-List-with-Random-Pointer.py)
- 1.copy node # 1->1'->2->2'->3->3': newnode.next=p.next, p.next=newnode, p=newnode.next
- 2.copy random for 1', 2': p.next.random = p.random.next, random.next is copied newnode with same value***
- 3.split two linkedlist: cur = dummy and p form -1 and head, skip every other, return dummy.next
- Time: O(n), Space: O(1)

### [2. Add Two Numbers](https://github.com/liangliang1120/leetcode/blob/main/solutions/2-Add-Two-Numbers.py)
- Time: O(max(m,n)), Space: O(1)

### [141. Linked List Cycle](https://github.com/liangliang1120/leetcode/blob/main/solutions/0141-Linked-List-Cycle.py)
- template for cycle linkedlist: slow, fast = head, head.next; while fast and fast.next:
- Time: O(n), Space: O(1)

### [287. Find the Duplicate Number](https://github.com/liangliang1120/leetcode/blob/main/solutions/0287-Find-the-Duplicate-Number.py)
- get the point meet first time; then meet: the result
- Time: O(n), Space: O(1)



