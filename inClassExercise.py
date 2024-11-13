def DFS(V, E):
    def __visit(i, count):
        V[i], count = count, count + 1
        for e in E:
            if (e[0] == i) and (V[e[1]] == -1):
                count = __visit(e[1], count)
            elif (e[1] == i) and (V[e[0]], count):
                count = __visit(e[0], count)
        return count
    
    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            count = __visit(i, count)


V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
E = [
    ['A', 'E', 1],
    ['A', 'H', 1],
    ['B', 'A', 1],
    ['C', 'F', 1],
    ['C', 'G', 1],
    ['D', 'A', 1],
    ['D', 'E', 1],
    ['E', 'C', 1],
    ['F', 'D', 1],
    ['F', 'E', 1],
    ['G', 'B', 1],
    ['G', 'E', 1],
    ['H', 'D', 1]
]

# ===================================================
DFS(V, E)