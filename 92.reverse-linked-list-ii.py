#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        sublist_head = prev.next
        current_node = sublist_head
        
        reversed_sublist_head = None
        
        for _ in range(right - left + 1):
            next_node = current_node.next
            current_node.next = reversed_sublist_head
            reversed_sublist_head = current_node
            current_node = next_node
            
        prev.next = reversed_sublist_head
        sublist_head.next = current_node
        
        return dummy.next
# @lc code=end
