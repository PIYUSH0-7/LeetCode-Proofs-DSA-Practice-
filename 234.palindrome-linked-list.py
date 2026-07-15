#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find the middle of the list using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Helper function to reverse a linked list
        def reverseList(node):
            prev = None
            curr = node
            while curr:
                next_node_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_node_temp
            return prev
        
        # Reverse the second half of the list starting from 'slow'
        second_half_head = reverseList(slow)

        # Compare the first half with the reversed second half
        first_half_ptr = head
        reversed_second_half_ptr = second_half_head
        while reversed_second_half_ptr: # Iterate until the end of the reversed second half
            if first_half_ptr.val != reversed_second_half_ptr.val:
                return False
            first_half_ptr = first_half_ptr.next
            reversed_second_half_ptr = reversed_second_half_ptr.next
        
        return True
# @lc code=end
