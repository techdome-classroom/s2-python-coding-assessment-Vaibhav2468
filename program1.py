class Solution(object):
    def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    
    # HashMap to match closing and opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Traverse through the string
    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            # Check if the stack is non-empty and the top of the stack is the matching opening bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push to the stack
            stack.append(char)
    
    # In the end, stack should be empty if all brackets were matched
    return not stack

# Test cases
print(isValid("()"))      # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False









    



  

