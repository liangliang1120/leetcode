# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque([(root, 1)])
        res = 0
        level = 0
        while q:
            size = len(q)
            temp = []
            for i in range(size):
                cur = q.popleft()
                index = cur[1]
                temp.append((cur[0].val, index))
                if cur[0].left:
                    q.append((cur[0].left, index * 2))
                if cur[0].right:
                    q.append((cur[0].right, index * 2 + 1))
            # print(temp)
            # print(temp[-1])
            temp_width = temp[-1][1] - temp[0][1] + 1
            if res < temp_width:
                res = temp_width
            level += 1
        return res
