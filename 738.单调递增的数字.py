#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        flag = len(str(n))
        res = list(str(n))
        for i in range(len(str(n)) - 1, 0, -1):
            if int(res[i]) < int(res[i - 1]):
                flag = i
                res[i - 1] = str(int(res[i - 1]) - 1)
                res[i:] = ['9'] * (len(res) - i)
        return int(''.join(res[:flag] + ['9'] * (len(res) - flag)))
# @lc code=end

