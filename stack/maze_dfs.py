from stack.array_stack import ArrayStack

map =[[ '1', '1', '1', '1', '1', '1' ],
      [ 'e', '0', '0', '0', '0', '1' ],
      [ '1', '0', '1', '0', '1', '1' ],
      [ '1', '1', '1', '0', '0', 'x' ],
      [ '1', '1', '1', '0', '1', '1' ],
      [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6

# 갈 수 있는 위치인지를 판단하는 알고리즘
def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE: # 미로 범위 안에 있는 좌표인지 검사
        if map[y][x] == "0" or map[y][x] == "x": # 통로/도착점 중 하나인지 검사
            return True
    return False

def DFS():
    print("DFS: ")
    stack = ArrayStack(100)
    stack.push((0, 1)) # 시작위치 삽입

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end="->")
        (x, y) = here # 스택에서 꺼낸 값을 튜플로 저장

        if map[y][x] == "x":
            return True
        else:
            map[y][x] = "." # 현재위치에 방문 표시
            if isValidPos(x, y-1): # 위쪽 이동 가능하면
                stack.push((x, y-1)) # 해당 좌표 스택에 삽입
            if isValidPos(x, y+1):
                stack.push((x, y+1))
            if isValidPos(x-1, y):
                stack.push((x-1, y))
            if isValidPos(x+1, y):
                stack.push((x+1, y))
        print("현재 스택: ", stack)
    return False

result = DFS()
if result: print("--> 미로탐색 성공")
else: print("--> 미로탐색 실패")