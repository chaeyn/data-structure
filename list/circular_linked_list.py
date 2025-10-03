class Node:
    def __init__(self, elem, next=None):
        self.data = elem # 노드가 저장할 데이터 필드
        self.link = next # 다음 노드를 가리키는 링크 필드

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self): return self.size == 0

    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:  # 시작 노드에서 pos번 링크를 따라 움직이면 pos 위치 노드에 도착
            node = node.link
            pos -= 1
        return node

    def insert(self, pos, elem):
        newNode = Node(elem)
        if self.isEmpty(): # 빈 연결 리스트
            newNode.link = newNode # 자기 자신 가리킴
            self.head = newNode
        elif pos <= 0: # 맨 앞에 삽입
            tail = self.getNode(self.size -1) # 마지막 노드를 tail로 정의
            newNode.link = self.head # newNode의 link를 원래 맨 앞 노드를 가리키게
            self.head = newNode # head가 newNode를 가리키게
            tail.link = newNode # 마지막 노드의 link가 newNode를 가리키게
        elif 0 < pos <= self.size: # 중간/맨 뒤 삽입
            before = self.getNode(pos-1) # pos의 전 노드를 before로 정의
            newNode.link =  before.link # newNode의 link가 pos를 가리키게
            before.link = newNode # pos의 전 노드가 newNode를 가리키게
        self.size += 1 # 새로운 노드가 추가되었으니 사이즈 증가

    def delete(self, pos):
        if self.isEmpty() or pos < 0 or pos >= self.size:
            return # 리스트가 비었거나 유효하지 않은 pos값인 경우
        if self.size == 1: # node가 하나만 있는 경우
            self.head = None # head가 가리키는 것이 없게
        elif pos == 0: # 맨 앞 노드를 삭제
            tail = self.getNode(self.size-1)
            self.head = self.head.link # 맨 앞 노드가 가리키는 노드를 head로
            tail.link = self.head # tail이 새로운 head를 가리키게
        else: # 중간/맨 뒤 삭제
            before = self.getNode(pos-1)
            before.link = before.link.link # 건너뛰기
        self.size -= 1

    def __str__(self):
        if self.isEmpty():
            return "[]"
        arr = []
        node = self.head
        for _ in range(self.size): # 원형 연결 리스트는 순환하므로 size만큼만 반복
            arr.append(node.data)
            node = node.link
        return str(arr)


if __name__ == "__main__":
    clist = CircularLinkedList()

    print("최초   ", clist)
    clist.insert(0, 10)
    clist.insert(0, 20)
    clist.insert(1, 30)
    clist.insert(3, 40)
    clist.insert(2, 50)
    print("삽입x5 ", clist)

    print("\n순환 확인:")
    node = clist.head
    for i in range(8):
        print(node.data, end=" → ")
        node = node.link
    print("...\n")

    print("2번째 값:", clist.getNode(2).data)
    clist.delete(2)
    print("삭제(2)", clist)
    clist.delete(3)
    print("삭제(3)", clist)
    clist.delete(0)
    print("삭제(0)", clist)

    if not clist.isEmpty():
        tail = clist.getNode(clist.size - 1)
        print(f"\ntail이 head를 가리키나?  {tail.link == clist.head}")