#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while prev.next and prev.next.next:
            first_node = prev.next
            second_node = prev.next.next
            
            # Swap the two nodes
            first_node.next = second_node.next
            second_node.next = first_node
            prev.next = second_node
            
            # Move prev to the first_node (which is now after second_node)
            # to prepare for the next pair
            prev = first_node
            
        return dummy.next
# @lc code=end
