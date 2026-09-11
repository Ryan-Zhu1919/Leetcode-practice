#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and s[i] not in 'aeiouAEIOU':
                i += 1
            while j >= 0 and s[j] not in 'aeiouAEIOU':
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
# @lc code=end

