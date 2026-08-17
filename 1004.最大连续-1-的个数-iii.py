#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = k
        cnt = Counter()
        left = 0
        for right, c in enumerate(nums):
            cnt[c] += 1
            while cnt[0] > k:
                if nums[left] == 0:
                    cnt[0] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end