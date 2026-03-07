import math
from typing import List
from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
        self.fuel = 0
        def dfs(node,parent):
            people = 1
            for nei in graph[node]:
                if nei != parent:
                    people+= dfs(nei , node)
            if node != 0:
                self.fuel += math.ceil(people/seats)
            return people
        dfs(0,-1)
        return self.fuel