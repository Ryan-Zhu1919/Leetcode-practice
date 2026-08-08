#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        step = [0] * (n + 1)
        step[0] = 1
        step[1] = 1
        for i in range(2, n + 1):
            step[i] = step[i - 1] + step[i - 2]
        return step[n]
# @lc code=end

