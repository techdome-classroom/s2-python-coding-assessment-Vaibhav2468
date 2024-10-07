class Solution(object):
    def isValid(self,s):
   
       stack = []

    # Map of closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Loop over each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the last opened bracket from the stack
            top_element = stack.pop() if stack else '#'
            
            # If the popped element does not match the expected opening bracket, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # If the character is an opening bracket, push it to the stack
            stack.append(char)

    # If the stack is empty, it means all brackets were matched correctly
    return len(stack) == 0











    



  

