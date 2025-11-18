# 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited):
    print(vtx[s], end=" ")  # 현재 정점 s를 출력함
    visited[s] = True  # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)):  # 인접행렬
        if adj[s][v] != 0:  # 모든 간선 (s,v)에 대해
            if visited[v] == False:  # v를 아직 방문하지 않았으면
                DFS(vtx, adj, v, visited)


# 깊이 우선 탐색 테스트 프로그램
vtx = ["A", "B", "C", "D", "E", "F", "G", "H"]
edge = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

print("DFS(출발:A) : ", end="")
DFS(vtx, edge, 0, [False] * len(vtx))
print()
