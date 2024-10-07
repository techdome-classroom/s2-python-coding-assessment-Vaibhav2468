class Solution(object):
    def isValid(self,s):
   
    stack = []
    
  
    bracket_map = {')': '(', '}': '{', ']': '['}
    

    for char in s:
        if char in bracket_map:  # If it's a closing bracket
ening bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push to the stack
            stack.append(char)
    
    # In the end, stack should be empty if all brackets were matched
    return not stack










    



  

