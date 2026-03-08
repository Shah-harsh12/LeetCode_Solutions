class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(0)
        n = len(s)
        if n < 2:
            return False
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif (char == ')' or char == '}' or char == ']') and stack[-1] == 0:
                return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if stack[-1] == 0:
            return True
        else: 
            return False