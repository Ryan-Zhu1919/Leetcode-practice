#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if n < 2:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
# @lc code=end

