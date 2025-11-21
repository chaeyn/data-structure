# 중간 과정 출력용 함수
def print_step(arr, val):
    print(" Step %2d = " % val, end="")
    print(arr)


def insertion_sort(A):
    n = len(A)  # n, 리스트 A의 길이
    for i in range(1, n):  # 1, 2, . . . , n-1 외부 루프
        key = A[i]  # 삽입할 항목
        j = i - 1
        # 삽입할 위치를 찾기 위한 내부 루프
        while j >= 0 and A[j] > key:  # 비교 연산
            A[j + 1] = A[j]  # 항목 이동
            j -= 1
        A[j + 1] = key  # 삽입
        print_step(A, i)  # 중간 과정 출력용 문장


if __name__ == "__main__":
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    data = list(org)
    print("Original  :", org)
    insertion_sort(data)
    print("Insertion :", data)
