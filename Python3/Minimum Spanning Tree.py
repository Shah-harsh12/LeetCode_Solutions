import heapq

class Solution:
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u,v,w in edges:
            adj[v].append((u,w))
            adj[u].append((v,w))
        
        visited = [False]*V
        mst_weight = 0
        min_heap = [(0,0)]
        while min_heap:
            weight,node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            mst_weight += weight
            
            for nei , wt in adj[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap,(wt,nei))
            
        return mst_weight