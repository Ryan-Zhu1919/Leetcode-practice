#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                right = max(right, intervals[i][1])
            else:
                res.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        res.append([left, right])
        return res
# @lc code=end

