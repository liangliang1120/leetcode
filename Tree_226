# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         self.traverse(root)
#         return root

#     def traverse(self, root):
#         if not root:
#             return

#         temp = root.left
#         root.left = root.right
#         root.right = temp
#         self.traverse(root.left)
#         self.traverse(root.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
        
        
        
