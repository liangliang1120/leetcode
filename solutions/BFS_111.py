# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            leftd = self.minDepth(root.left)
            rightd = self.minDepth(root.right)
            return min(leftd, rightd) +1

        # q = collections.deque([root])
        # level = 1
        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         cur = q.popleft()
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        #         if not cur.left and not cur.right:
        #             return level
        #     level += 1
        # return level
