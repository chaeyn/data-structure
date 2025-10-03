class Node:
    def __init__(self, elem, next=None):
        self.data = elem # 노드가 저장할 데이터 필드
        self.link = next # 다음 노드를 가리키는 링크 필드

class LinkedList:
    def __init__(self):
        self.head = None # 시작 노드를 가리킴

    def isEmpty(self):
        return self.head == None # head가 None이면 공백 상태

    def isFull(self):
        return False # 연결 리스트에서는 포화 상태가 의미가 없다 -> Flase 반환

    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None: # 시작 노드에서 pos번 링크를 따라 움직이면 pos 위치 노드에 도착
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos):
        node = self.getNode(pos) # pos 위치의 노드를 먼저 구한다
        if node == None: return None
        else: return node.data # 구한 노드의 데이터 필드를 반환

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None: # 맨 앞에거 삭제 시
            if self.head is not None: # head가 있다면
                self.head = self.head.link # head를 다음 노드로 변경
        elif before.link != None: # before.link가 삭제할 노드를 가리키니까 True
            before.link = before.link.link # 삭제할 노드의 전 노드가 삭제할 노드의 다음 노드를 가리게 변경 (건너뛰기)
            # 마지막 요소를 삭제하는 경우 None을 가리키게 됨

    def __str__(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)

if __name__ == "__main__":
    L = LinkedList()

    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    print("연결리스트 3번째 값: ", L.getEntry(2))
    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)