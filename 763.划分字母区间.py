#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import List
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        left, right = 0, 0
        hashmap = {}
        for i, c in enumerate(s):
            hashmap[c] = i
        for i, c in enumerate(s):
            right = max(right, hashmap[c])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res
# @lc code=end

