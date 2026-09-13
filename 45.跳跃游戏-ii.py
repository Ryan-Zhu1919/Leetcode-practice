#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps
# @lc code=end

