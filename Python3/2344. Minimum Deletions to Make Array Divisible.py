import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for num in numsDivide:
            g = math.gcd(g,num)
        nums.sort()
        for i in range(len(nums)):
            if g%nums[i] == 0:
                return i
        
        return -1