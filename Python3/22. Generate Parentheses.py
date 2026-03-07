from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current:str , open_count:int , closed_count:int , maxcount:int):
            if len(current) == maxcount*2:
                result.append(current)
                return
            if open_count < maxcount:
                backtrack(current + "(", open_count +1 , closed_count , maxcount)
            if closed_count < open_count:
                backtrack(current + ")", open_count , closed_count+1 , maxcount)
        backtrack("",0,0,n)
        return result
        