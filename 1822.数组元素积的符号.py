#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            elif nums[i] < 0:
                nums[i] = -1
            else:
                nums[i] = 1
            ans *= nums[i]
        return ans
# @lc code=end

