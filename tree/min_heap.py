def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i // 2
        if heap[pi] <= n:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n


def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while i <= size:
        if i < size and heap[i] > heap[i + 1]:
            i += 1
        if last <= heap[i]:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root


if __name__ == "__main__":
    # 최소힙 테스트 프로그램
    data = [2, 5, 4, 8, 9, 3, 7, 3]  # 힙에 삽입할 데이터
    heap = [0]
    print("입력", data)
    for e in data:
        heappush(heap, e)  # 모든 데이터를 힙에 삽입
        print("heap : ", heap[1:])  # 삽입 연산
    print("삭제:", heappop(heap))  # 삭제
    print("heap:", heap[1:])
    print("삭제:", heappop(heap))  # 삭제
    print("heap:", heap[1:])
