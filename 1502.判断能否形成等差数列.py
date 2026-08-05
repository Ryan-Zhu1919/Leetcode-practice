#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        for i in range(len(arr) - 2):
            if arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]:
                return False
        return True   
# @lc code=end

