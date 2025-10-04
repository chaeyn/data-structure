class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None # 시작 노드를 가리키는 top

    def isEmpty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top) # 현재 top을 가리키는 새 노드를 생성하고 top을 새로 생성한 노드로 변경

    def peek(self):
        if not self.isEmpty():
            return self.top.data # 공백이 아니면 상단 노드의 데이터 반환

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link # 다음 노드를 top으로 지정
            return data

    def size(self):
        node = self.top
        count = 0
        while not node is None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr = []
        node = self.top
        while not node is None:
            arr.append(node.data)
            node = node.link
        return str(arr)

if __name__ == "__main__":
    s = LinkedStack() # 스택 객체를 생성

    print("스택: ", s)
    msg = input("문자열 입력: ") # 문자열을 입력받음
    for c in msg : # 문자열의 각 문자 c에 대해
        s.push(c) # c를 스택에 삽입

    print("스택: ", s)

    print("문자열 출력: ", end='')
    while not s.isEmpty(): # 스택이 공백상태가 아니라면
        print(s.pop(), end='') # 하나의 요소를 꺼내서 출력
    print()
    print("스택: ", s)
