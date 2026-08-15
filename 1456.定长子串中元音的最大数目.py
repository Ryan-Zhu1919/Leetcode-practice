#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, res = 0, 0
        for i, word in enumerate(s):
            if word in "aeiou":
                res += 1
            if i < k - 1:
                continue
            ans = max(ans, res)
            if s[i - k + 1] in "aeiou":
                res -= 1
        return ans
# @lc code=end