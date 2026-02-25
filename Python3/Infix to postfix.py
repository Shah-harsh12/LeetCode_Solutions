class Solution:
    def infixtoPostfix(self, s):
        stack = []
        result = ""
        precedence = {'^' : 3 , '/' : 2 ,'*' : 2 ,'+' : 1 ,'-' : 1 }
        
        for char in s:
            
            if char.isalnum():
                result += char
                
            elif char == '(':
                stack.append(char)
                
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                     
                stack.pop()
            
            else:
                while stack and stack[-1] != '(' and ( precedence[char] < precedence[stack[-1]] or (precedence[char] == precedence[stack[-1]] and char != '^')) :
                    result += stack.pop()
                stack.append(char)
        
        while stack:
            result += stack.pop()
        
        return result
                
            
        
        