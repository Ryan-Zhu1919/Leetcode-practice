#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary) - 2
        a = min(salary)
        b = max(salary)
        c = sum(salary)
        return (c - a - b) / n
# @lc code=end

