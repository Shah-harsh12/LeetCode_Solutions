from collections import deque

class Solution:
    def bfs(self, adj):
        v = len(adj)
        visited = [False]*v
        q = deque()
        result = []
        visited[0] = True
        q.append(0)
        
        while q:
            node = q.popleft()
            result.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
        return result