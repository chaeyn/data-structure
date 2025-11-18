# 코드: 딕셔너리(리스트 기반) 깊이 우선 탐색(DFS, 재귀)
def DFS2(graph, v, visited):
    if v not in visited:  # v가 아직 방문되지 않았다면
        visited.add(v)  # v 방문 표시
        print(v, end=" ")  # v 출력
        for u in graph[v]:  # v의 모든 인접 정점 u에 대해
            if u not in visited:  # 방문하지 않은 정점이면
                DFS2(graph, u, visited)  # 재귀 호출 (순환)


# 그래프를 딕셔너리(리스트)로 표현
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "G", "H"],
    "F": ["D"],
    "G": ["E", "H"],
    "H": ["E", "G"],
}

visited = set()  # 방문한 정점 기록용 집합
print("DFS2(출발:A): ", end="")
DFS2(graph, "A", visited)
print()
