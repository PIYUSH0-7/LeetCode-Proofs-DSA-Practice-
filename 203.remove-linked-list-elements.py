#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next
# @lc code=end
