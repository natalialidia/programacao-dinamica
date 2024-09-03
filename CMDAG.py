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

    result.reverse()
    return result

# Calcular caminho mínimo de s para todo outro vértice
def CMDAG(G, l, s):
    ts = toposort(G)
    dist = [float('inf') for i in range(len(G))]
    pai = [-1 for i in range(len(G))]
    
    dist[s] = 0
    pai[s] = -1

    G_s = [v for v in ts if v != s]
    print(G_s)
    for v in G_s:
        uv = [dist[u]+l[f"{u}-{v}"] if v in G[u] else float('inf') for u in G]
        dist[v] = min(uv)
        pai[v] = uv.index(min(uv))

    return dist, pai

grafo = {
    0: [1, 2], # nó a
    1: [2], # nó b
    2: [4], # nó c
    3: [1, 4, 5], # nó d
    4: [5, 6], # nó e
    5: [7], # nó f
    6: [5, 8], # nó g
    7: [], # nó h
    8: [5, 7] # nó i
}

pesos = {
    '0-1': 1,
    '0-2': 2,
    '1-2': 1,
    '2-4': 1,
    '3-1': 3,
    '3-4': 2,
    '3-5': 1,
    '4-5': 4,
    '4-6': 5,
    '5-7': 1,
    '6-5': 3,
    '6-8': 2,
    '8-5': 2,
    '8-7': 4
}

dist, pai = CMDAG(grafo, pesos, 0)
print(dist)

print('caminho de a para h:')

p = 8
while pai[p] != -1:
    print(p)
    p = pai[p]