from circular_queue import *

class CircularDeque(CircularQueue):
    def __init__(self, capaticy=10):
        super().__init__(capaticy) # 부모 클래스의 생성자를 호출

    # 원형 덱과 동작이 동일한 연산
    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    # 새로 구현이 필요한 연산
    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item # 현재의 front에 새로운 요소 저장
            self.front = (self.front - 1 + self.capacity) % self.capacity # front를 반시계 방향으로 한 칸 회전
        else: pass

    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear] # 현재 rear 요소 저장
            self.rear = (self.rear - 1 + self.capacity) % self.capacity # rear를 반시계 방향으로 한 칸 회전
            return item # 저장(삭제)한 요소 반환
        else: pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i%2==0 : dq.addRear(i)
        else : dq.addFront(i)
    print("홀수->전단, 짝수->후단:", dq)

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    print(" 전단삭제x2 후단삭제x3:", dq)

    for i in range(9,14): dq.addFront(i)
    print("   전단삽입 9,10,...13:", dq)