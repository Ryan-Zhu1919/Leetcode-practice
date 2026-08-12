#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, 1
        while right < n:
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
# @lc code=end

