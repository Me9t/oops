import numpy as np

# Merge Sort Algorithm (Divide and Conquer)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# Strassen's Matrix Multiplication (Divide and Conquer)
def strassen_multiply(A, B):
    assert A.shape == B.shape and len(A.shape) == 2, "Matrices must be square and of same dimensions"

    n = A.shape[0]

    # If n is not a power of 2, pad the matrices with zeros
    m = 1
    while m < n:
        m *= 2
    if m > n:
        A_padded = np.zeros((m, m))
        B_padded = np.zeros((m, m))
        A_padded[:n, :n] = A
        B_padded[:n, :n] = B
        C_padded = strassen_multiply(A_padded, B_padded)
        return C_padded[:n, :n]

    if n == 1:
        return A * B

    mid = n // 2

    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

# Example Usage
if __name__ == "__main__":
    # Merge Sort Example
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted Array:", merge_sort(arr))

    # Strassen's Matrix Multiplication Example
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("Strassen's Matrix Multiplication Result:\n", strassen_multiply(A, B))
