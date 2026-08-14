#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            s = (right - left) * min(height[left], height[right])
            ans = max(ans, s)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
# @lc code=end

