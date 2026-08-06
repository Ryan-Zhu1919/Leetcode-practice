#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i,j = 0, 0
        for a in moves:
            if a == 'U':
                i += 1
            elif a == 'D':
                i -= 1
            elif a == 'L':
                j -= 1
            elif a == 'R':
                j += 1
        return i == 0 and j == 0
# @lc code=end

