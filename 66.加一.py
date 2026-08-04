#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] +=1
                return digits
            else:
                digits[i] = 0
                i -= 1
        return [1] + digits
# @lc code=end

