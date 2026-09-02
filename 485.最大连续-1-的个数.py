#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#
from typing import List
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, ans = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans
# @lc code=end

