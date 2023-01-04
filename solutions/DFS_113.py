# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.res = []
        def dfs(root, target, path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and sum(path) == target:
                self.res.append(path[:])
            else:
                dfs(root.left, target, path)
                dfs(root.right, target, path)
            path.pop()
        dfs(root, targetSum, [])
        return self.res

    
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(curr_node, curr_path, curr_sum):
            if not curr_node.left and not curr_node.right and curr_sum == targetSum:
                res.append(curr_path.copy())
                return
            else:
                return
            
            for next_node in (curr_node.left, curr_node.right):
                if not next_node:     #注意：这里不用判断加入next_node后sum是不是比targetSum大，因为后面的node可能为负值
                    continue

                curr_path.append(next_node.val)   #这里不能放进下一行为啥？curr_path.append()没有返回值，下一行需要一个数组
                backtrack(next_node, curr_path, curr_sum + next_node.val)
                curr_path.pop()
        
        if not root:
            return []
        
        res = []
        backtrack(root, [root.val], root.val)
        return res
