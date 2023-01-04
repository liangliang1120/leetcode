class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            for node in nestedList:
                if node.isInteger():
                    self.sum += node.getInteger() * depth
                else:
                    dfs(node.getList(), depth + 1)
        self.sum = 0
        dfs(nestedList, 1)
        return self.sum
