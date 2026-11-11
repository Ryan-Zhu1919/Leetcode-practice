#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 纯暴力
        # while True:
        #     changed = False
        #     for i in range(len(nums) - 1):
        #         if nums[i] > nums[i + 1]:
        #             nums[i], nums[i + 1] = nums[i + 1], nums[i]
        #             changed = True
        #     if not changed:
        #         break 
        pos0 = pos1 = 0
        for i, num in enumerate(nums):
            nums[i] = 2
            if num < 2:
                nums[pos1] = 1
                pos1 += 1
            if num == 0:
                nums[pos0] = 0
                pos0 += 1
# @lc code=end

