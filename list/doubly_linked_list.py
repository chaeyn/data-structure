class DoublyNode:
    def __init__(self, elem, llink=None, rlink=None):
        self.data = elem # 노드의 데이터 필드
        self.llink = llink # 이전 노드를 가리키는 링크
        self.rlink = rlink # 다음 노드를 가리키는 링크

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self): return self.size == 0

    def getNode(self, pos):
        if pos < 0 or pos >= self.size:
            return None
        node = self.head
        while pos > 0 and node != None:  # 시작 노드에서 pos번 링크를 따라 움직이면 pos 위치 노드에 도착
            node = node.rlink
            pos -= 1
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos-1)

        # 맨 앞에 삽입
        if before is None:
            newNode = DoublyNode(elem, None, self.head) # 새로운 노드 생성, 이전 노드 없음, 다음 노드 현재 맨 앞 노드
            if self.head is not None: # 다음 노드가 있다면
                self.head.llink = newNode # 현재 head의 이전 노드를 newNode로 지정
            self.head = newNode # head를 newNode로 변경

        # 중간/마지막에 삽입
        else:
            newNode = DoublyNode(elem, before, before.rlink) # 이전 노드, 이전 노드의 다음 노드를 가리키는 newNode 생성
            if before.rlink is not None: # 이전 노드의 다음 노드가 있다면
                before.rlink.llink = newNode # 원래 pos 위치 노드의 llink를 newNode로 변경
            before.rlink = newNode # 이전 노드의 다음 노드는 newNode를 가리키게

        self.size += 1

    def delete(self, pos):
        target = self.getNode(pos)

        # 맨 앞의 경우
        if target.llink is None:
            self.head = target.rlink # head를 삭제할 요소의 다음 요소로 변경
            if self.head is not None: # 다음 요소가 있다면
                self.head.llink = None # head의 이전 요소를 삭제

        # 중간/마지막의 경우
        else:
            target.llink.rlink = target.rlink # target 이전 요소의 rlink가 target 다음 요소를 가리키게
            if target.rlink is not None: # target 다음 요소가 있다면
                target.rlink.llink = target.llink # target 다음 요소의 llink가 target의 이전 요소를 가리키게

        self.size -= 1

    def __str__(self):
        if self.isEmpty():
            return "[]"
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.rlink
        return str(arr)

    def printReverse(self):
        if self.isEmpty():
            return "[]"
        arr = []
        node = self.getNode(self.size - 1)
        # 맨 마지막 node에서 이전으로 이동하며 array에 넣기
        while node is not None:
            arr.append(node.data)
            node = node.llink
        return str(arr)


if __name__ == "__main__":
    D = DoublyLinkedList()

    print("최초   ", D)
    D.insert(0, 10)
    D.insert(0, 20)
    D.insert(1, 30)
    D.insert(3, 40)
    D.insert(2, 50)
    print("삽입x5 ", D)
    print("역순   ", D.printReverse())

    print("\n2번째 값:", D.getNode(2).data)
    D.delete(2)
    print("삭제(2)", D)
    D.delete(3)
    print("삭제(3)", D)
    D.delete(0)
    print("삭제(0)", D)
    print("역순   ", D.printReverse())