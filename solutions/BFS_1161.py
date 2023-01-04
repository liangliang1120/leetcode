# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        max_level = 1
        max_sum = float('-inf')
        q = collections.deque([root])
        level = 1
        while q:
            size = len(q)
            level_sum = 0
            for i in range(size):
                cur = q.popleft()
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if max_sum < level_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        return max_level
            
