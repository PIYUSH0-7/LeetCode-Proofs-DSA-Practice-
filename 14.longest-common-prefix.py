#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # The first string serves as our reference to build the prefix.
        # Its length also defines the maximum possible length for the common prefix.
        first_str = strs[0]
        
        # Iterate through each character of the first string.
        for i in range(len(first_str)):
            char_to_match = first_str[i]
            
            # Compare this character with the character at the same position
            # in all other strings in the list.
            for j in range(1, len(strs)):
                # If the current string `strs[j]` is shorter than the current index `i`,
                # or if the character at position `i` in `strs[j]` does not match
                # `char_to_match`, then we've found the end of the common prefix.
                if i >= len(strs[j]) or strs[j][i] != char_to_match:
                    # Return the portion of `first_str` that matched so far.
                    return first_str[:i]
        
        # If the loop completes, it means all characters of `first_str`
        # were found to be common prefixes among all other strings.
        # In this case, `first_str` itself is the longest common prefix.
        return first_str
# @lc code=end
