#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur = num
                count = 1
                while cur + 1 in nums_set:
                    cur += 1
                    count += 1
                ans = max(ans, count)
        return ans
# @lc code=end

