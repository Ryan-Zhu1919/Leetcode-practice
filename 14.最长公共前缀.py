#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for j, c in enumerate(s0):  # 从左到右
            for s in strs:  # 从上到下
                if j == len(s) or s[j] != c: 
                    return s0[:j]  
        return s0
# @lc code=end

