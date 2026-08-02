#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            ans = max(ans, score)
        return ans    
# @lc code=end

