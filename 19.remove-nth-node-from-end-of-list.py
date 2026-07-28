#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        slow = dummy
        fast = dummy
        
        # Move fast pointer n+1 steps ahead of the slow pointer.
        # This creates a gap such that when fast reaches the end,
        # slow will be at the node immediately preceding the one to be removed.
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until the fast pointer reaches the end of the list (None).
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # At this point, slow.next is the node to be removed.
        # Skip the target node by linking slow.next to slow.next.next.
        slow.next = slow.next.next
        
        # The new head of the list is dummy.next.
        return dummy.next
# @lc code=end
