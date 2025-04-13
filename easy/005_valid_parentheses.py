#problem(5) ////////////////  Valid Parentheses ////////////////////////////////
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""
#####
"""def isValid( s: str):
    d = { '(' : ')',
          '[' : ']',
          '{' : '}'
        }
    if not s :
         return False
    for i,ch in enumerate(s):
        print("i = ",i)
        if ch in d :
            index_char = s.find(d[ch])
            print("index = " , index_char)
            if index_char == -1 :
                return False          
    return True

    
#print(isValid("([)]"))
print(isValid("([])"))"""
def isValid(s):
    # Initialize a stack to be used in the algorithm.
    stack = []
    
    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}
    
    # For every character in the input string
    for char in s:
        
        # If the character is an closing bracket
        if char in mapping:
            
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            #top_element = stack.pop() if stack else '#'
            if stack:
                 top_element = stack.pop()
                 """print("top_element : ",top_element)
                 print("stak : " , stack)"""
            else:
                 top_element = '#'
                 
            
            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)
    
    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack
#print(isValid("((()"))