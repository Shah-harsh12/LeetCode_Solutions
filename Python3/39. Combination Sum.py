from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target ,0 , [] , result)
        return result
    def backtrack(self, candidates: List[int], target: int, start : int, temp : List[int], result: List[List[int]]) :
        if target == 0:
            result.append(list(temp))
            return
        for i in range(start , len(candidates)):
            if target >= candidates[i]:
                temp.append(candidates[i])
                self.backtrack(candidates, target - candidates[i], i , temp , result)
                temp.pop()
        return result