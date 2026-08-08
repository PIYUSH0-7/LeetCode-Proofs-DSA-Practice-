#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less_ptr = less_head
        greater_ptr = greater_head
        
        current = head
        while current:
            if current.val < x:
                less_ptr.next = current
                less_ptr = less_ptr.next
            else:
                greater_ptr.next = current
                greater_ptr = greater_ptr.next
            current = current.next
        
        greater_ptr.next = None
        
        less_ptr.next = greater_head.next
        
        return less_head.next
# @lc code=end
