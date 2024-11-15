# Takes an array (A), starting index (start) and final index (end). Returns the element with the smallest value.
def Min(A, start, end):
    print(f"START = {A[start]}, END = {A[end]}")
    if (start == end):
        return end
    else:
        mid = (end + start) // 2
        first = Min(A, start, mid)
        last = Min(A, mid + 1, end)
        print(f"Returning {A[first] if A[first] < A[last] else A[last]}")
        return first if A[first] < A[last] else last
    
A3 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A4 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A5 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

# ================================================
print(Min(A3, 0, len(A3)-1))
print(Min(A4, 0, len(A4)-1))
print(Min(A5, 0, len(A5)-1))