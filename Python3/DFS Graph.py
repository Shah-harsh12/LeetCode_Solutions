class Solution:
    def dfs(self, adj):
        visited = [False]*len(adj)
        result = []
        def dfsutil(node):
            visited[node] = True
            result.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    dfsutil(nei)
        dfsutil(0)
        return result
        