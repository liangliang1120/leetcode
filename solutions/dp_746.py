class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * n
        minCost[1] = min(cost[0], cost[1])
        for i in range(2, n):
            minCost[i] = min(minCost[i - 1] + cost[i], minCost[i - 2] + cost[i - 1])
        return minCost[-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost0, minCost1 = 0, min(cost[0], cost[1])
        for i in range(2, len(cost)):
            minCost = min(minCost1 + cost[i], minCost0 + cost[i - 1])
            minCost0, minCost1 = minCost1, minCost;
        return minCost
