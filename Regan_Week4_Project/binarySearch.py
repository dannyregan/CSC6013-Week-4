# Accepts an array (A), starting index (start), final index (end), and element to search for (k). Returns the index of the element k or returns None if it doesn't exist.
def binarySearch(A, start, end, k):
    mid = (start + end) // 2
    if (start > end):
        return None
    elif (A[mid] == k):
        return mid
    elif (A[mid] < k):
        return binarySearch(A, start, mid-1, k)
    else:
        return binarySearch(A, mid + 1, end, k)


A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
k1 = 44
k2 = 56
k3 = 42

A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]
k4 = -1
k5 = -7
# =====================================================
print(binarySearch(A1, 0, len(A1)-1, k1))
print(binarySearch(A1, 0, len(A1)-1, k2))
print(binarySearch(A1, 0, len(A1)-1, k3))
print(binarySearch(A2, 0, len(A1)-1, k4))
print(binarySearch(A2, 0, len(A1)-1, k5))