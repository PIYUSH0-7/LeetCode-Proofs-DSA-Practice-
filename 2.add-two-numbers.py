#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            totalSum = val1 + val2 + carry
            digit = totalSum % 10
            carry = totalSum // 10
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummyHead.next
# @lc code=end
