class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 1
        for i in range(n - 1):
            curr_step = step1
            step1 = step1 + step2
            step2 = curr_step
        return step1
    


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         p = 0
#         q = 0
#         r = 1
#         for i in range(n):
#             p = q
#             q = r
#             r = p + q
#         return r


class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. determine the dp and [i]
        # dp[i]: to claim to i th floor stairs, have i ways

        # 2. formuna
        # dp[i] = dp[i - 1] + dp[i - 2]

        # array initialization
        # dp[1] = 1，dp[2] = 2

        # Traversal order
        # 从前往后

        # exampleexample
        # i:     1 2 3 4 5
        # dp[i]: 1 2 3 5 8
        
        dp = [0 for _ in range(n + 1)] 
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
