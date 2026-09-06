#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True
        return False
# @lc code=end

