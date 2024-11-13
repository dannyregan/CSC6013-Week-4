def DFSDirected(V, E):
    def __visit(i, count):
        print(f"Vertex {VLetters[i]} visited and received the stamp {count}")
        # print(VLetters[i])
        # print(count)
        print(f"DFS called for vertex {VLetters[i]}")
        V[i], VLetters[i], count = count, count, count + 1
        for e in E:
            if (e[0] == i) and (V[e[1]] == -1):
                print(f"Current array: {VLetters}")
                count = __visit(e[1], count)
        return count
    
    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            count = __visit(i, count)
    print(f"Current array: {VLetters}")

# Accounts for graphs that are bidirectional.
def DFSBidirectional(V, E):
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


VLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
V = [0] * 8
# E = [
#     ['A', 'E', 1],
#     ['A', 'H', 1],
#     ['B', 'A', 1],
#     ['C', 'F', 1],
#     ['C', 'G', 1],
#     ['D', 'A', 1],
#     ['D', 'E', 1],
#     ['E', 'C', 1],
#     ['F', 'D', 1],
#     ['F', 'E', 1],
#     ['G', 'B', 1],
#     ['G', 'E', 1],
#     ['H', 'D', 1]
# ]

E = [
    [0, 4, 1],  # 'A' - 'E'
    [0, 7, 1],  # 'A' - 'H'
    [1, 0, 1],  # 'B' - 'A'
    [2, 5, 1],  # 'C' - 'F'
    [2, 6, 1],  # 'C' - 'G'
    [3, 0, 1],  # 'D' - 'A'
    [3, 4, 1],  # 'D' - 'E'
    [4, 2, 1],  # 'E' - 'C'
    [5, 3, 1],  # 'F' - 'D'
    [5, 4, 1],  # 'F' - 'E'
    [6, 1, 1],  # 'G' - 'B'
    [6, 4, 1],  # 'G' - 'E'
    [7, 3, 1]   # 'H' - 'D'
]

# ===================================================
DFSDirected(V, E)