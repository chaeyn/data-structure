def print_step(arr, val):
    print(f" Step {val} = ", end="")
    print(arr)

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        b_changed = False
        for j in range(i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                b_changed = True
        if not b_changed: break;
        print_step(A, n-i)

if __name__ == "__main__":
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    data = list(org)
    print("Original :", org)
    bubble_sort(data)
    print("Bubble :", data)
