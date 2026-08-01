#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
     n = 0
     for j in range(len(nums)):
        for i in range(j):
            if nums[i] == nums[j]:
                n += 1   
     return n
# @lc code=end

