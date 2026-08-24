#
# @lc app=leetcode.cn id=2487 lang=python3
#
# [2487] 从链表中移除节点
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        head = reverse(head)
        max_val = float('-inf')
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val < max_val:
                cur.next = cur.next.next
            else:
                max_val = cur.next.val
                cur = cur.next
        return reverse(dummy.next)
# @lc code=end

