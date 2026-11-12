#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i, num in enumerate(nums):
            if count[num] > 1:
                return num
# @lc code=end

