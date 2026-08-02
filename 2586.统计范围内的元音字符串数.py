#
# @lc app=leetcode.cn id=2586 lang=python3
#
# [2586] 统计范围内的元音字符串数
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                ans += 1
        return ans
# @lc code=end

