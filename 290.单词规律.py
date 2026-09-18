#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashtable = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hashtable:
                if s[i] in hashtable.values():
                    return False
                hashtable[pattern[i]] = s[i]
            else:
                if hashtable[pattern[i]] != s[i]:
                    return False
        return True
# @lc code=end

