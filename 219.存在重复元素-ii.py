#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, x in enumerate(nums):
            if x in s:
                return True
            s.add(x)
            if i >= k:
                s.remove(nums[i - k])
        return False
# @lc code=end

