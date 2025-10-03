capacity = 100 # 리스트 용량 지정
array = [None] * capacity # 길이가 capacity인 빈 배열 생성
size = 0 # 리스트 항목들의 개수 공백상태(0)로 초기화

def isEmpty():
    if size == 0: return True
    else: return False

def isFull():
    return size == capacity

def insert(pos, e):
    global size # size는 전역적으로 수정이 가능 해야 하므로 전역 변수 선언
    if not isFull() and 0 <= pos <= size: # 포화 상태가 아니고 pos가 유효한 위치이면
        for i in range(size, pos, -1): # pos부터 size-1까지 모든 항목을 한 칸씩 뒤로 옮기면 -> pos 자리가 빈다
            array[i] = array[i-1] # 새로운 자리 할당 -> 앞에꺼 밀기
        array[pos] = e # 빈 pos 자리에 새로운 요소 추가
        size += 1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

def delete(pos):
    global size
    if not isEmpty() and 0 <= pos <= size:
        e = array[pos]
        for i in range(pos, size-1): # pos+1부터 size-1까지 모든 항목을 한 칸씩 앞으로 옮겨 덮어씀
            array[i] = array[i+1]
        size -= 1 # size를 감소시켜 사이즈 뒤의 인덱스는 무시
        return e # 삭제한 요소 반환
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

def getEntry(pos):
    if 0 <= pos < size: # pos가 유효한 위치이면 array[pos] 반환
        return array[pos]
    else: return None

if __name__ == "__main__":
    print("최초  ", array[0:size])
    insert(0, 10)
    insert(0, 20)
    insert(1, 30)
    insert(size, 40)
    insert(2, 50)
    print("삽입x5", array[0:size])
    delete(2)
    print("삭제(2)", array[0:size])
    delete(size-1)
    print("삭제(E)", array[0:size])
    delete(0)
    print("삭제(0)", array[0:size])