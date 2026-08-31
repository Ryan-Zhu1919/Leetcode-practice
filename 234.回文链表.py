#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self,head: Optional[ListNode]):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseNode(self,head: Optional[ListNode]):
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseNode(mid)
        while head2:
            if head.val != head2.val:
                self.reverseNode(head2)
                return False
            head = head.next
            head2 = head2.next
        self.reverseNode(head2)
        return True
# @lc code=end

