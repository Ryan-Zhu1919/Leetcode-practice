#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        self.backtracking(s, 0, 0, "", res)
        return res

    def backtracking(self, s, startindex, pointsum, path, res):
        if pointsum > 3:
            return
        if pointsum == 3:
            if self.isvalid(s, startindex, len(s) - 1):
                path += s[startindex:]
                res.append(path)
            return
        for i in range(startindex, len(s)):
            if self.isvalid(s, startindex, i):
                path + s[startindex:i + 1] + "."
                self.backtracking(s, i + 1, pointsum + 1, path + s[startindex:i + 1] + ".", res)

    def isvalid(self, s, start, end):
        if start > end:
            return False
        if s[start] == "0" and start != end:
            return False
        num = int(s[start:end + 1])
        return 0 <= num <= 255
# @lc code=end

