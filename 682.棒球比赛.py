#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for a in operations:
            if a == 'C':
                res.pop()
            elif a == 'D':
                res.append(res[-1] * 2)
            elif a == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(a))
        return sum(res)
# @lc code=end

