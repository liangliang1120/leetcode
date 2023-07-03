
### [226. Invert Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/0226-Invert-Binary-Tree.py)
- left = self.invertTree(root.left)
- right = self.invertTree(root.right)
- root.left = right
- root.right = left
- Time: O(N), Space:O(n)

### [104. Maximum Depth of Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/0104-Maximum-Depth-of-Binary-Tree.py)
- Time: O(N), Space:O(height)
