#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n, rightmost = len(nums), 0
        # for i in range(n):
        #     if i <= rightmost:
        #         rightmost = max(rightmost, i + nums[i])
        #         if rightmost >= n - 1:
        #             return True
        # return False
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach, i + nums[i])
                if max_reach >= n - 1:
                    return True
# @lc code=end

