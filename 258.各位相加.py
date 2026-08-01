#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
       num = str(num)
       while len(num) > 1:
           res = 0
           for i in num:
               res += int(i)
           num = str(res)
       return int(num)
# @lc code=end

