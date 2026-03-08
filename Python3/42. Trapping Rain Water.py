from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0]*n
        rightmax = [0]*n
        leftmax[0] = height[0]
        for i in range(1 , n):
            leftmax[i] = max(leftmax[i-1] , height[i])
        rightmax[n-1] = height[n-1]
        for i in range(n-2 , -1 , -1):
            rightmax[i] = max(rightmax[i+1] , height[i])
        rain_water = 0
        for i in range(n):
            rain_water += min(rightmax[i], leftmax[i]) - height[i]
        return rain_water    