#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        
        if n < 4 or n > 12:
            return []

        results = []
        current_ip_parts = []

        def is_valid_part(part_str: str) -> bool:
            if len(part_str) > 1 and part_str[0] == '0':
                return False
            
            num = int(part_str)
            return 0 <= num <= 255

        def backtrack(index: int, num_parts: int):
            if num_parts == 4:
                if index == n:
                    results.append(".".join(current_ip_parts))
                return

            if index == n:
                return

            for i in range(index, min(index + 3, n)):
                part_str = s[index : i + 1]
                if is_valid_part(part_str):
                    current_ip_parts.append(part_str)
                    backtrack(i + 1, num_parts + 1)
                    current_ip_parts.pop()

        backtrack(0, 0)
        return results
# @lc code=end
