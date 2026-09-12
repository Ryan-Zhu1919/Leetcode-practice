#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[n-2]:
                nums[n] = nums[i]
                n += 1
        return n
# @lc code=end

