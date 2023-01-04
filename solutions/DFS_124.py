# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getSum(root):
            if not root:
                return 0

            leftSum = getSum(root.left)
            rightSum = getSum(root.right)
            sumTemp = leftSum + rightSum + root.val
            self.res = max(self.res, sumTemp)

            return max(0, max(leftSum, rightSum) + root.val) 

        getSum(root)
        return self.res
