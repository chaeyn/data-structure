class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    # 공백상태와 포화상태의 코드가 서로 같아 구분이 되지 않는다
    # -> 하나의 자리를 비워두는 전략을 사용한다
    # --> front가 rear의 바로 다음에 있으면 포화 상태라고 정의한다
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity # rear를 시계방향으로 한 칸 회전
            self.array[self.rear] = item # 그 위치에 새로운 요소 넣기
        else: pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass

    # 맨 앞 요소를 들여다보는 peek
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity] # front의 다음 위치의 요소 반환
        else: pass

    def size(self):
        # 원형 큐는 사이즈가 음수가 될 수 있다.
        # -> (rear - front + capacity) % capacity로 해결
        return (self.rear + self.front + self.capacity) % self.capacity

    def __str__(self):
        # 일반적으로 생각하는 경우
        if self.front < self.rear:
            return str(self.array[self.front+1:self.rear+1])
        # front가 rear보다 큰 경우
        # -> front+1 ~ capacity-1, 0 ~ rear 출력
        else:
            return str(self.array[self.front+1:self.capacity] + self.array[0:self.rear+1])

if __name__ == "__main__":
    q = CircularQueue(8)
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print('A B C D E F 삽입: ', q)
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('      3번의 삭제: ', q)
    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')
    print('      G H I 삽입: ', q)