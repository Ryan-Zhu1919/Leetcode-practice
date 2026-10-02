#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        res = 1
        points.sort(key=lambda x: x[0])
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                res += 1
            else:
                points[i][1] = min(points[i][1], points[i - 1][1])
        return res
# @lc code=end

