

def toposort(G):
    visited = [False for i in range(len(G))]
    result = []

    def DFS(node):
        if visited[node]:
            return
        visited[node] = True
        for adj in G[node]:
              DFS(adj)
        result.append(node)
    
    for i in range(len(G)):
        DFS(i)

    return result

# Calcular caminho mínimo de s para todo outro vértice
def CMDAG(G, l, s):
    G = toposort(G)
    dist = [None for i in range(len(G))]
    
    dist[s] = 0

    G_s = (v for v in range(len(G)) if v != s)
    for v in range(len(G_s)):
        uv = ((u+l[u][v]) for u in G_s if G_s[u][v] != None)
        dist[v] = min(uv)
    return dist
