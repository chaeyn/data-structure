# 려거 개의 리스트를 사용하기 위해 클래스로 구현

class ArrayList:
    # 리스트의 데이터를 생성자에서 정의, 초기화
    # 생성자는 객체가 생성 될 때 실행되는 초기화 함수
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else: pass

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else: pass

    def __str__(self):
        return str(self.array[0:self.size]) # 리스트에 실제로 들어 있는 요소(size만큼)만 문자열로 반환
        # __str__() 메소드가 없다면 객체의 메모리 주소가 출력된다

if __name__ == "__main__":
    L = ArrayList(100)
    print("최초  ", L.array[0:L.size])
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(L.size, 40)
    L.insert(2, 50)
    print("삽입x5", L.array[0:L.size])
    L.delete(2)
    print("삭제(2)", L.array[0:L.size])
    L.delete(L.size-1)
    print("삭제(E)", L.array[0:L.size])
    L.delete(0)
    print("삭제(0)", L.array[0:L.size])