class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        height_diff = height(root.left) - height(root.right)
        return abs(height_diff) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
