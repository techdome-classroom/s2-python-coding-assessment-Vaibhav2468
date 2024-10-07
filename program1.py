class Solution(object):
    def isValid(self,s):
   
       stack = []

    # Map of closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

   
    for char in s:
        
        if char in bracket_map:
           
            top_element = stack.pop() if stack else '#'
            
            
            if bracket_map[char] != top_element:
                return False
        else:
            # If the character is an opening bracket, push it to the stack
            stack.append(char)

    # If the stack is empty, it means all brackets were matched correctly
    return len(stack) == 0











    



  

