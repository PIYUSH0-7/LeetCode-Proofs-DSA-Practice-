#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. Find the length of the list and the last node
        n = 1
        current = head
        while current.next:
            current = current.next
            n += 1
        
        # 'current' is now the last node (tail)
        tail = current 

        # 2. Make the list circular
        tail.next = head

        # 3. Calculate effective rotations
        k_eff = k % n

        # 4. Find the new tail
        # The new tail will be (n - k_eff - 1) steps from the original head.
        # The node after this new tail will be the new head.
        steps_to_new_tail = n - k_eff - 1
        
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # 5. Determine the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
# @lc code=end
