#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent, late = 0, 0
        for i, c in enumerate(s):
            if c == 'A':
                absent += 1
                if absent >= 2:
                    return False
            if c == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True
# @lc code=end

