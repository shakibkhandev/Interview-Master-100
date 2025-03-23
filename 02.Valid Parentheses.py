# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# SOLUTION
# To solve this problem, we can use a stack. We'll iterate through each character in the string. If we encounter an opening bracket, we'll push it onto the stack. If we encounter a closing bracket, we'll check if the stack is empty or if the top of the stack doesn't match the corresponding opening bracket. If either condition is true, we return false. If not, we pop the top element from the stack.

# After processing all characters, we check if the stack is empty. If it is, all brackets were properly closed, and we return true. If not, there are unmatched opening brackets, so we return false.

# The time complexity of this solution is O(n), where n is the length of the input string. We iterate through each character once, and stack operations (push and pop) are O(1).


class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in bracket_pairs:
                if not stack or bracket_pairs[char] != stack.pop():
                    return False    
            else:
                stack.append(char)
                
        return not stack
    


# Test cases

print(Solution().isValid("()"))  # True
print(Solution().isValid("()[]{}"))  # True
print(Solution().isValid("(]"))  # False
print(Solution().isValid("([])"))  # True