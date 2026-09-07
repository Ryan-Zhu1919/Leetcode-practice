#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            s = str(nums[start])
            if start < i:
                s += "->" + str(nums[i])
            ans.append(s)
            i += 1
        return ans
# @lc code=end

