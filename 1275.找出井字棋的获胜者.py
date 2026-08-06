#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = [[(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 0), (2, 0)],
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],
                [(0, 2), (1, 1), (2, 0)]]
        A_set = set()
        B_set = set()
        for i, move in enumerate(moves):
            if i % 2 == 0:
                A_set.add(tuple(move))
            else:
                B_set.add(tuple(move))
            for win in wins:
                if all(step in A_set for step in win):
                    return "A"
                if all(step in B_set for step in win):
                    return "B"
        return "Draw" if len(moves) == 9 else "Pending"
# @lc code=end

