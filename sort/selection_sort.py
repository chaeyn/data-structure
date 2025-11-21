# 중간 과정 출력용 함수
def print_step(arr, val):
    print(" Step %2d = " % val, end="")
    print(arr)


# 선택 정렬 알고리즘
def selection_sort(A):
    n = len(A)  # n, 리스트 A의 길이
    for i in range(n - 1):  # 0, 1, 2, . . . , n-2 외부 루프
        least = i
        # 최솟값 위치를 저장할 변수
        for j in range(i + 1, n):  # i+1, . . . , n-1 내부 루프
            if A[j] < A[least]:  # 비교 연산
                least = j  # 최소 항목 갱신
        if least != i:
            temp = A[i]  # 배열 항목 교환
            A[i] = A[least]
            A[least] = temp
            print_step(A, i + 1)
            # 중간 과정 출력용 문장


if __name__ == "__main__":
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    data = list(org)
    print("Original  :", org)
    selection_sort(data)
    print("Selection :", data)
