#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            a = mat[i][i] + mat[i][len(mat) - 1 - i]
            res += a
        if len(mat) % 2 != 0:
            ans = res - mat[len(mat) // 2][len(mat) // 2]
        else:
            ans = res
        return ans
# @lc code=end

