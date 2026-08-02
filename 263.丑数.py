#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for a in [2, 3, 5]:
            while n % a == 0:
                n //= a
        return n == 1
# @lc code=end

