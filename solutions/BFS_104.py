# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        level = 0
        while q:
            level += 1
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return level
