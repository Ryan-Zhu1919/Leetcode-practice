#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in group:
                group[sorted_s] = []
            group[sorted_s].append(s)
        return list(group.values())
# @lc code=end

