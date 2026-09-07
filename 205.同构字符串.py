#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for a, b in zip(s, t):
            if a in dic1 and dic1[a] != b:
                return False
            if b in dic2 and dic2[b] != a:
                return False
            dic1[a] = b
            dic2[b] = a
        return True
# @lc code=end

