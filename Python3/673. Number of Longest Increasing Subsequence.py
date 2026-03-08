from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        length = [1]*n
        count = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] +1 > length[i]:
                        length[i] = length[j] + 1
                    elif length[j] +1 == length[i]:
                        count[i] = count[j] + 1
        maxlen = max(length)
        result = 0
        for i in range(n):
            if length[i] == maxlen:
                result += count[i]
        return result