#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # Check if curr is the start of a duplicate sequence
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value as curr
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # After the loop, curr is at the last duplicate node.
                # Link prev.next to the node after the duplicate sequence.
                prev.next = curr.next
                # Move curr to the node after the duplicate sequence
                curr = curr.next
            else:
                # No duplicate found, advance both pointers
                prev = curr
                curr = curr.next
        
        return dummy.next
# @lc code=end
