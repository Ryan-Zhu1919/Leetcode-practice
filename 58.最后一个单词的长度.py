#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1, -1,-1):
            if s[i] != ' ':
                ans += 1
            elif ans > 0:
                return ans
        return ans
# @lc code=end

