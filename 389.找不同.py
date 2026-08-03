#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
         s = sorted(s)
         t = sorted(t)
         if len(s) == 0:
              return t[0]
         for i in range(len(s)):
              if s[i] != t[i]:
                   return t[i]
         return t[-1]          
# @lc code=end

