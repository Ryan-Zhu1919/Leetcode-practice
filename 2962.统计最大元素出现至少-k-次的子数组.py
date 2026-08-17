#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#
from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        m = max(nums)
        left = cnt_m = 0
        for x in nums:
            if x == m:
                cnt_m += 1
            while cnt_m == k:
                if nums[left] == m:
                    cnt_m -= 1
                left += 1
            ans += left
        return ans
# @lc code=end

