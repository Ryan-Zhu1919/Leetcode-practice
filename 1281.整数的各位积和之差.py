#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        a = 1
        b = 0
        for i in n:
            a *= int(i)
            b += int(i)
        return a - b
# @lc code=end

