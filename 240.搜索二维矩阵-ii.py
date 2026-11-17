#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, 0
        while m >= 0 and n < len(matrix[0]):
            if matrix[m][n] > target:
                m -= 1
            elif matrix[m][n] < target:
                n += 1
            else:
                return True
        return False
# @lc code=end

